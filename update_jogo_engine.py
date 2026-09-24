# -*- coding: utf-8 -*-
"""
Updates jogo.html to include:
1. Realistic PIT SJC campus masterplan layout (Rodovia Pres. Dutra BR-116, Av. Dr. Altino Bondesan,
   Campus UNIFESP ICT, Nexus Hub, Centro de Governança OS, Pavilhão Aeroespacial com mockup Embraer,
   Living Lab Net-Zero com lago e usina solar, heliponto, estacionamentos e áreas verdes do Vale do Paraíba).
2. Animated walking avatar ('bonequinho') with swinging legs, arms, walking dust particles,
   bobbing torso, blazer/tie, and facing direction.
3. Explicit Phase naming: FASE 1, FASE 2, FASE 3, FASE 4, FASE 5, FASE 6 across the HUD,
   direction banner, buildings, and question modal.
4. GAME_RESET listener that resets points, unlocks all 6 phases, clears storage, and opens register modal.
"""

import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
jogo_path = os.path.join(script_dir, "jogo.html")

with open(jogo_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update Direction Banner HTML to show Fase explicitly
code = code.replace(
    '<span id="target-label">Caminhe até o Bloco Acadêmico UNIFESP</span>',
    '<span id="target-label">Vá até a FASE 1: Bloco Acadêmico UNIFESP</span>'
)

# 2. Update the stations array and coordinates for realistic 1920x1380 masterplan
old_stations_pattern = re.compile(r'/\* Station Coordinates on the 1600x1200 Campus Map \*/\s*const stations = \[.*?\];', re.DOTALL)

new_stations_code = '''/* Station Coordinates on the Realistic 1920x1380 PIT SJC Masterplan Map */
    const stations = [
      { id: 1, block: 1, phaseNum: 1, name: "Bloco Acadêmico UNIFESP", phaseLabel: "FASE 1", fullName: "FASE 1 • Bloco Acadêmico UNIFESP", x: 340, y: 360, radius: 95, icon: "🎓", color: "#38bdf8", subtitle: "Campus ICT • Fundamentos Teóricos & Moore (1993)" },
      { id: 2, block: 2, phaseNum: 2, name: "Praça Central das Hélices", phaseLabel: "FASE 2", fullName: "FASE 2 • Praça Central das Hélices", x: 780, y: 720, radius: 95, icon: "🌀", color: "#a855f7", subtitle: "Rotatória Central • As 5 Hélices & Interdependência" },
      { id: 3, block: 3, phaseNum: 3, name: "Centro de Governança do PIT", phaseLabel: "FASE 3", fullName: "FASE 3 • Centro de Governança do PIT", x: 1140, y: 920, radius: 100, icon: "🏛️", color: "#f59e0b", subtitle: "Administração OS • Orquestração Machado et al." },
      { id: 4, block: 4, phaseNum: 4, name: "Nexus Hub de Startups", phaseLabel: "FASE 4", fullName: "FASE 4 • Nexus Hub de Startups", x: 1160, y: 520, radius: 95, icon: "🚀", color: "#06b6d4", subtitle: "Incubadora & Aceleradora • Furr & Shipilov" },
      { id: 5, block: 5, phaseNum: 5, name: "Pavilhão Aeroespacial & San Diego", phaseLabel: "FASE 5", fullName: "FASE 5 • Pavilhão Aeroespacial & San Diego", x: 1560, y: 440, radius: 105, icon: "✈️", color: "#10b981", subtitle: "Hangares CDT • Benchmarking Internacional" },
      { id: 6, block: 6, phaseNum: 6, name: "Living Lab Net-Zero & Fronteiras", phaseLabel: "FASE 6", fullName: "FASE 6 • Living Lab Net-Zero & Fronteiras", x: 680, y: 1140, radius: 100, icon: "🌱", color: "#f43f5e", subtitle: "Área de Preservação • Shen et al. & Fronteiras" }
    ];'''

code = old_stations_pattern.sub(new_stations_code, code)

# 3. Update the Canvas Engine, Animated Avatar and Realistic PIT SJC Map rendering
# Find from /* 2D Canvas & Player Engine */ to /* Kahoot Challenge Engine */
engine_pattern = re.compile(r'/\* 2D Canvas & Player Engine \*/.*?/\* Kahoot Challenge Engine \*/', re.DOTALL)

new_engine_code = '''/* 2D Canvas & Player Engine */
    const canvas = document.getElementById('rpg-canvas');
    const ctx = canvas.getContext('2d');
    const minimapCanvas = document.getElementById('minimap-canvas');
    const minimapCtx = minimapCanvas.getContext('2d');

    const WORLD_W = 1920;
    const WORLD_H = 1380;

    // Animated Avatar Character ("Bonequinho Andando")
    const hero = {
      x: 400,
      y: 450,
      radius: 20,
      speed: 5.2,
      vx: 0,
      vy: 0,
      targetX: null,
      targetY: null,
      facing: 'right', // 'left', 'right', 'up', 'down'
      isMoving: false,
      walkCycle: 0,
      particles: [] // Walking dust puffs
    };

    const keys = {};

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Controls listeners
    window.addEventListener('keydown', (e) => {
      keys[e.code] = true;
      keys[e.key] = true;
      hero.targetX = null;
      hero.targetY = null;
      if (e.code === 'KeyE' || e.code === 'Space') {
        checkNearbyStationInteraction();
      }
    });
    window.addEventListener('keyup', (e) => {
      keys[e.code] = false;
      keys[e.key] = false;
    });

    // Click/Touch to walk on canvas
    canvas.addEventListener('pointerdown', (e) => {
      const camX = Math.max(0, Math.min(WORLD_W - canvas.width, hero.x - canvas.width / 2));
      const camY = Math.max(0, Math.min(WORLD_H - canvas.height, hero.y - canvas.height / 2));
      hero.targetX = e.clientX + camX;
      hero.targetY = e.clientY + camY;
    });

    // Mobile Virtual Joystick setup
    const joystickZone = document.getElementById('joystick-zone');
    const joystickKnob = document.getElementById('joystick-knob');
    let joyActive = false;
    let joyStart = { x: 0, y: 0 };
    let joyDelta = { x: 0, y: 0 };

    if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
      joystickZone.style.display = 'block';
      document.getElementById('btn-action-mobile').style.display = 'flex';

      joystickZone.addEventListener('touchstart', (e) => {
        joyActive = true;
        const t = e.touches[0];
        const rect = joystickZone.getBoundingClientRect();
        joyStart = { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
        hero.targetX = null;
        hero.targetY = null;
      });

      window.addEventListener('touchmove', (e) => {
        if (!joyActive) return;
        const t = e.touches[0];
        const dx = t.clientX - joyStart.x;
        const dy = t.clientY - joyStart.y;
        const dist = Math.hypot(dx, dy);
        const maxDist = 35;
        const angle = Math.atan2(dy, dx);
        const clampedDist = Math.min(dist, maxDist);
        joyDelta = { x: Math.cos(angle) * (clampedDist / maxDist), y: Math.sin(angle) * (clampedDist / maxDist) };
        joystickKnob.style.transform = `translate(${Math.cos(angle) * clampedDist}px, ${Math.sin(angle) * clampedDist}px)`;
      });

      const endJoy = () => {
        joyActive = false;
        joyDelta = { x: 0, y: 0 };
        joystickKnob.style.transform = `translate(0px, 0px)`;
      };
      window.addEventListener('touchend', endJoy);
      window.addEventListener('touchcancel', endJoy);

      document.getElementById('btn-action-mobile').addEventListener('click', () => {
        checkNearbyStationInteraction();
      });
    }

    /* Main Game Loop */
    let animTime = 0;
    function gameLoop() {
      try {
        updateHero();
        renderScene();
        renderMinimap();
      } catch (err) {
        console.error("Game loop error:", err);
      }
      requestAnimationFrame(gameLoop);
    }

    function updateHero() {
      let dx = 0;
      let dy = 0;

      if (keys['KeyW'] || keys['ArrowUp'] || keys['w'] || keys['W']) dy -= 1;
      if (keys['KeyS'] || keys['ArrowDown'] || keys['s'] || keys['S']) dy += 1;
      if (keys['KeyA'] || keys['ArrowLeft'] || keys['a'] || keys['A']) dx -= 1;
      if (keys['KeyD'] || keys['ArrowRight'] || keys['d'] || keys['D']) dx += 1;

      if (joyActive && (Math.abs(joyDelta.x) > 0.1 || Math.abs(joyDelta.y) > 0.1)) {
        dx = joyDelta.x;
        dy = joyDelta.y;
      } else if (hero.targetX !== null && hero.targetY !== null) {
        const dist = Math.hypot(hero.targetX - hero.x, hero.targetY - hero.y);
        if (dist < 8) {
          hero.targetX = null;
          hero.targetY = null;
        } else {
          dx = (hero.targetX - hero.x) / dist;
          dy = (hero.targetY - hero.y) / dist;
        }
      }

      const len = Math.hypot(dx, dy);
      if (len > 0.05) {
        hero.isMoving = true;
        hero.x += (dx / (len > 1 ? len : 1)) * hero.speed;
        hero.y += (dy / (len > 1 ? len : 1)) * hero.speed;
        hero.walkCycle += 0.28;

        if (Math.abs(dx) > Math.abs(dy)) {
          hero.facing = dx > 0 ? 'right' : 'left';
        } else {
          hero.facing = dy > 0 ? 'down' : 'up';
        }

        // Emit walking dust particle under shoes
        if (Math.random() < 0.45) {
          hero.particles.push({
            x: hero.x + (Math.random() - 0.5) * 12,
            y: hero.y + 16,
            radius: Math.random() * 3 + 2,
            alpha: 0.6
          });
        }
      } else {
        hero.isMoving = false;
      }

      // Update dust particles
      for (let i = hero.particles.length - 1; i >= 0; i--) {
        const p = hero.particles[i];
        p.alpha -= 0.035;
        p.radius *= 0.96;
        if (p.alpha <= 0) {
          hero.particles.splice(i, 1);
        }
      }

      // Constrain within world
      hero.x = Math.max(hero.radius + 20, Math.min(WORLD_W - hero.radius - 20, hero.x));
      hero.y = Math.max(hero.radius + 40, Math.min(WORLD_H - hero.radius - 20, hero.y));
    }

    function renderScene() {
      animTime += 0.03;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Camera offset centered on animated hero
      const camX = Math.max(0, Math.min(WORLD_W - canvas.width, hero.x - canvas.width / 2));
      const camY = Math.max(0, Math.min(WORLD_H - canvas.height, hero.y - canvas.height / 2));

      ctx.save();
      ctx.translate(-camX, -camY);

      // 1. Realistic Campus Masterplan Ground (PIT SJC - Eugênio de Melo)
      drawCampusGround();

      // 2. Render Stations & Realistic Buildings
      stations.forEach(st => {
        drawStation(st);
      });

      // 3. Target Waypoint Indicator
      if (hero.targetX !== null) {
        ctx.beginPath();
        ctx.arc(hero.targetX, hero.targetY, 12 + Math.sin(animTime * 4) * 4, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(6, 182, 212, 0.85)";
        ctx.lineWidth = 2.5;
        ctx.stroke();
      }

      // 4. Draw Animated Walking Avatar ("Bonequinho Andando")
      drawHero();

      ctx.restore();
    }

    /* REALISTIC PIT SJC CAMPUS MASTERPLAN RENDERING */
    function drawCampusGround() {
      // 1. Base terrain (Vale do Paraíba landscape)
      ctx.fillStyle = "#070f1e";
      ctx.fillRect(0, 0, WORLD_W, WORLD_H);

      // Grassy polygons and landscaped parcels
      ctx.fillStyle = "#0a192f";
      ctx.fillRect(80, 240, 520, 360);   // UNIFESP Academic Sector
      ctx.fillRect(940, 380, 480, 360);  // Nexus Innovation Sector
      ctx.fillRect(1380, 240, 480, 460); // Aerospace & CDT Sector
      ctx.fillRect(940, 780, 500, 380);  // Governance & OS Sector
      ctx.fillRect(400, 960, 580, 360);  // Net-Zero Ecological Reserve

      // 2. NORTH: Rodovia Presidente Dutra (BR-116)
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(0, 30, WORLD_W, 100);
      
      // Highway lane divider
      ctx.strokeStyle = "#eab308";
      ctx.lineWidth = 3;
      ctx.setLineDash([20, 15]);
      ctx.beginPath();
      ctx.moveTo(0, 80);
      ctx.lineTo(WORLD_W, 80);
      ctx.stroke();
      ctx.setLineDash([]);

      // Highway Guard-Rails & Highway Sign
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(0, 25, WORLD_W, 5);
      ctx.fillRect(0, 130, WORLD_W, 5);

      // Overhead Highway Signboard
      drawRoundRect(ctx, 640, 10, 480, 32, 6);
      ctx.fillStyle = "#065f46";
      ctx.fill();
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 1.5;
      ctx.stroke();
      ctx.fillStyle = "#fff";
      ctx.font = "bold 11px Outfit, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("🛣️ BR-116 PRES. DUTRA • KM 137 • PARQUE TECNOLÓGICO SJC (EUGÊNIO DE MELO)", 880, 30);

      // Access Viaduct and Main Entrance Portico (Guarita com Cancelas)
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(720, 130, 160, 140); // Entrance access road
      
      // Entrance Gate Canopy
      drawRoundRect(ctx, 680, 170, 240, 36, 8);
      ctx.fillStyle = "rgba(15, 23, 42, 0.95)";
      ctx.fill();
      ctx.strokeStyle = "#06b6d4";
      ctx.lineWidth = 2;
      ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 11px Outfit, sans-serif";
      ctx.fillText("PÓRTICO PRINCIPAL • PIT SJC", 800, 192);

      // 3. CENTRAL BOULEVARD: Av. Dr. Altino Bondesan (Double Avenue with Palms)
      ctx.fillStyle = "#162238";
      // Vertical main boulevard
      ctx.fillRect(730, 260, 140, 780);
      // Horizontal central arteries
      ctx.fillRect(120, 560, WORLD_W - 240, 100);
      ctx.fillRect(120, 920, 800, 80);

      // Central median with trees / palms
      ctx.fillStyle = "#0d233a";
      ctx.fillRect(795, 270, 10, 760);
      ctx.fillRect(130, 605, WORLD_W - 260, 10);

      // Road markings (white dashed lines)
      ctx.strokeStyle = "rgba(255, 255, 255, 0.25)";
      ctx.lineWidth = 2.5;
      ctx.setLineDash([14, 14]);
      
      ctx.beginPath();
      // Avenue lanes
      ctx.moveTo(765, 270); ctx.lineTo(765, 1030);
      ctx.moveTo(835, 270); ctx.lineTo(835, 1030);
      ctx.moveTo(130, 585); ctx.lineTo(WORLD_W - 130, 585);
      ctx.moveTo(130, 635); ctx.lineTo(WORLD_W - 130, 635);
      ctx.stroke();
      ctx.setLineDash([]);

      // 4. PEDESTRIAN CROSSINGS (Faixas de Pedestres Zebradas)
      drawCrosswalk(730, 370, 140, 25);
      drawCrosswalk(730, 530, 140, 25);
      drawCrosswalk(730, 665, 140, 25);
      drawCrosswalk(730, 860, 140, 25);
      drawCrosswalk(570, 560, 25, 100);
      drawCrosswalk(920, 560, 25, 100);

      // 5. HELIPONTO OFICIAL DO PIT (Near Governance Center)
      ctx.beginPath();
      ctx.arc(1360, 960, 55, 0, Math.PI * 2);
      ctx.fillStyle = "#1e293b";
      ctx.fill();
      ctx.strokeStyle = "#eab308";
      ctx.lineWidth = 4;
      ctx.stroke();
      ctx.fillStyle = "#eab308";
      ctx.font = "bold 44px Outfit, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("H", 1360, 976);
      ctx.font = "bold 9px JetBrains Mono, monospace";
      ctx.fillText("HELIPONTO PIT SJC", 1360, 1004);

      // 6. ECOLOGICAL LAKE (Living Lab Net-Zero - South Sector)
      ctx.beginPath();
      ctx.ellipse(680, 1180, 180, 90, -0.1, 0, Math.PI * 2);
      ctx.fillStyle = "#0c4a6e";
      ctx.fill();
      ctx.strokeStyle = "#0284c7";
      ctx.lineWidth = 3;
      ctx.stroke();

      // Wooden bridge over lake
      ctx.fillStyle = "#78350f";
      ctx.fillRect(660, 1090, 40, 180);
      ctx.fillStyle = "#b45309";
      for (let by = 1100; by < 1260; by += 15) {
        ctx.fillRect(662, by, 36, 3);
      }

      // Solar Farm (Painéis Solares Fotovoltaicos)
      for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 5; c++) {
          ctx.fillStyle = "#1e3a8a";
          ctx.fillRect(430 + c * 40, 1050 + r * 30, 32, 20);
          ctx.strokeStyle = "#38bdf8";
          ctx.lineWidth = 1;
          ctx.strokeRect(430 + c * 40, 1050 + r * 30, 32, 20);
        }
      }
      ctx.fillStyle = "#6ee7b7";
      ctx.font = "bold 9px JetBrains Mono, monospace";
      ctx.fillText("USINA SOLAR FOTOVOLTAICA NET-ZERO", 530, 1155);

      // 7. REALISTIC PARKING LOTS (Estacionamentos com Vagas e Carros)
      drawParkingLot(140, 410, 140, 100, "ESTACIONAMENTO UNIFESP");
      drawParkingLot(1280, 560, 140, 90, "ESTACIONAMENTO NEXUS");
      drawParkingLot(1440, 750, 140, 90, "ESTACIONAMENTO CDT / AERO");

      // 8. AEROSPACE MOCKUP JET (Patio Pavilhão Aeroespacial)
      drawMockupJet(1680, 360);
    }

    function drawCrosswalk(x, y, w, h) {
      ctx.fillStyle = "rgba(255, 255, 255, 0.4)";
      if (w > h) {
        for (let ix = x; ix < x + w; ix += 18) {
          ctx.fillRect(ix, y, 9, h);
        }
      } else {
        for (let iy = y; iy < y + h; iy += 18) {
          ctx.fillRect(x, iy, w, 9);
        }
      }
    }

    function drawParkingLot(x, y, w, h, label) {
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(x, y, w, h);
      ctx.strokeStyle = "rgba(255, 255, 255, 0.15)";
      ctx.lineWidth = 1.5;
      ctx.strokeRect(x, y, w, h);

      // Stalls
      ctx.strokeStyle = "rgba(255, 255, 255, 0.3)";
      ctx.lineWidth = 1;
      const numStalls = Math.floor(w / 24);
      for (let i = 0; i < numStalls; i++) {
        const sx = x + i * 24 + 4;
        ctx.strokeRect(sx, y + 4, 18, 38);
        ctx.strokeRect(sx, y + h - 42, 18, 38);
        
        // Random parked cars
        if ((i * 7) % 3 === 0) {
          ctx.fillStyle = (i % 2 === 0) ? "#38bdf8" : "#f43f5e";
          ctx.fillRect(sx + 3, y + 8, 12, 30);
        } else if ((i * 5) % 4 === 0) {
          ctx.fillStyle = "#e2e8f0";
          ctx.fillRect(sx + 3, y + h - 38, 12, 30);
        }
      }

      ctx.fillStyle = "#94a3b8";
      ctx.font = "bold 8px JetBrains Mono, monospace";
      ctx.textAlign = "center";
      ctx.fillText(label, x + w / 2, y + h / 2 + 3);
    }

    function drawMockupJet(x, y) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(-0.3);
      // Jet Fuselage
      ctx.fillStyle = "#e2e8f0";
      ctx.beginPath();
      ctx.ellipse(0, 0, 48, 12, 0, 0, Math.PI * 2);
      ctx.fill();
      // Wings
      ctx.fillStyle = "#94a3b8";
      ctx.beginPath();
      ctx.moveTo(-10, 0); ctx.lineTo(-20, -42); ctx.lineTo(10, -5);
      ctx.moveTo(-10, 0); ctx.lineTo(-20, 42); ctx.lineTo(10, 5);
      ctx.fill();
      // Cockpit
      ctx.fillStyle = "#0284c7";
      ctx.beginPath();
      ctx.ellipse(24, 0, 10, 5, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
      ctx.fillStyle = "#10b981";
      ctx.font = "bold 9px JetBrains Mono, monospace";
      ctx.textAlign = "center";
      ctx.fillText("MOCKUP AERONAVE EMBRAER", x, y + 55);
    }

    function drawRoundRect(targetCtx, x, y, width, height, radius) {
      const r = Math.min(radius, Math.min(width, height) / 2);
      targetCtx.beginPath();
      targetCtx.moveTo(x + r, y);
      targetCtx.lineTo(x + width - r, y);
      targetCtx.arcTo(x + width, y, x + width, y + r, r);
      targetCtx.lineTo(x + width, y + height - r);
      targetCtx.arcTo(x + width, y + height, x + width - r, y + height, r);
      targetCtx.lineTo(x + r, y + height);
      targetCtx.arcTo(x, y + height, x, y + height - r, r);
      targetCtx.lineTo(x, y + r);
      targetCtx.arcTo(x, y, x + r, y, r);
      targetCtx.closePath();
    }

    /* REALISTIC PIT SJC STATION BUILDINGS */
    function drawStation(st) {
      const isUnlocked = unlockedPhases.includes(st.block);
      const isCompleted = player.completedStations.includes(st.id);
      const dist = Math.hypot(st.x - hero.x, st.y - hero.y);
      const isNear = dist < st.radius + 35;

      // Pulsing Base Glow when active & unlocked
      if (isUnlocked && !isCompleted) {
        ctx.beginPath();
        ctx.arc(st.x, st.y, st.radius + Math.sin(animTime * 3) * 8, 0, Math.PI * 2);
        ctx.strokeStyle = `${st.color}44`;
        ctx.lineWidth = 4;
        ctx.stroke();
      }

      // Realistic Building Complex Box
      ctx.fillStyle = isUnlocked ? "rgba(15, 23, 42, 0.96)" : "rgba(10, 15, 26, 0.85)";
      ctx.strokeStyle = isCompleted ? "#10b981" : isUnlocked ? st.color : "rgba(255, 255, 255, 0.12)";
      ctx.lineWidth = isNear && isUnlocked ? 4 : 2;

      drawRoundRect(ctx, st.x - 90, st.y - 65, 180, 130, 16);
      ctx.fill();
      ctx.stroke();

      // Top Header Ribbon with PROMINENT PHASE NAME (FASE 1, FASE 2, etc.)
      drawRoundRect(ctx, st.x - 90, st.y - 65, 180, 26, 16);
      ctx.fillStyle = isCompleted ? "#065f46" : isUnlocked ? st.color : "#334155";
      ctx.fill();

      ctx.fillStyle = "#fff";
      ctx.font = "900 12px Outfit, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(st.phaseLabel + " • DESAFIO KAHOOT", st.x, st.y - 48);

      // Building Icon
      ctx.font = "28px sans-serif";
      ctx.fillText(st.icon, st.x, st.y - 12);

      // Station Name
      ctx.fillStyle = "#fff";
      ctx.font = "bold 11px Outfit, sans-serif";
      ctx.fillText(st.name, st.x, st.y + 16);

      // Subtitle / Concept reference
      ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
      ctx.font = "9px Outfit, sans-serif";
      ctx.fillText(st.subtitle.split("•")[1] || st.subtitle, st.x, st.y + 30);

      // Badge status
      ctx.font = "bold 10px JetBrains Mono, monospace";
      if (isCompleted) {
        ctx.fillStyle = "#6ee7b7";
        ctx.fillText("✓ CONCLUÍDO", st.x, st.y + 50);
      } else if (isUnlocked) {
        ctx.fillStyle = "#67e8f9";
        ctx.fillText("⭐ FASE ATIVA", st.x, st.y + 50);
      } else {
        ctx.fillStyle = "#94a3b8";
        ctx.fillText("🔒 BLOQUEADA", st.x, st.y + 50);
      }

      // Proximity Action Prompt
      if (isNear && isUnlocked && !isCompleted) {
        ctx.fillStyle = "rgba(6, 182, 212, 0.95)";
        drawRoundRect(ctx, st.x - 95, st.y - 100, 190, 28, 14);
        ctx.fill();

        ctx.fillStyle = "#000";
        ctx.font = "900 11px Outfit, sans-serif";
        ctx.fillText("💬 Clique ou Aperte E para Jogar!", st.x, st.y - 82);
      }
    }

    /* ANIMATED WALKING AVATAR ("BONEQUINHO ANDANDO") */
    function drawHero() {
      // 1. Draw walking dust particles
      hero.particles.forEach(p => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(148, 163, 184, ${p.alpha})`;
        ctx.fill();
      });

      // 2. Dynamic Shadow scaling with bobbing
      const bob = hero.isMoving ? Math.abs(Math.sin(hero.walkCycle)) * 3 : Math.sin(animTime * 2) * 1.2;
      ctx.beginPath();
      ctx.ellipse(hero.x, hero.y + 18, 16 - bob * 0.8, 7 - bob * 0.4, 0, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(0, 0, 0, 0.45)";
      ctx.fill();

      // 3. Pulsing Positioning Beacon Ring
      ctx.beginPath();
      ctx.arc(hero.x, hero.y + 16, 22 + Math.sin(animTime * 3) * 3, 0, Math.PI * 2);
      ctx.strokeStyle = "rgba(6, 182, 212, 0.55)";
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.save();
      ctx.translate(hero.x, hero.y - bob);

      // Facing orientation (flip horizontally if facing left)
      if (hero.facing === 'left') {
        ctx.scale(-1, 1);
      }

      // 4. ANIMATED LEGS & SHOES (Swinging stride)
      const legStride = hero.isMoving ? Math.sin(hero.walkCycle) * 9 : 0;
      
      // Left Leg & Shoe
      ctx.fillStyle = "#1e293b"; // Dark trousers
      ctx.fillRect(-8 - legStride * 0.4, 6, 6, 12);
      ctx.fillStyle = "#0f172a"; // Shoe
      ctx.fillRect(-10 - legStride * 0.4, 16, 10, 5);

      // Right Leg & Shoe
      ctx.fillStyle = "#334155";
      ctx.fillRect(2 + legStride * 0.4, 6, 6, 12);
      ctx.fillStyle = "#0f172a";
      ctx.fillRect(2 + legStride * 0.4, 16, 10, 5);

      // 5. TORSO & BUSINESS BLAZER (UNIFESP Royal Blue)
      ctx.fillStyle = "#1d4ed8";
      drawRoundRect(ctx, -10, -10, 20, 18, 5);
      ctx.fill();
      ctx.strokeStyle = "#60a5fa";
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // White shirt collar & Gold Tie
      ctx.fillStyle = "#f8fafc";
      ctx.beginPath();
      ctx.moveTo(-4, -10); ctx.lineTo(4, -10); ctx.lineTo(0, -4);
      ctx.fill();

      ctx.fillStyle = "#f59e0b"; // Gold tie
      ctx.beginPath();
      ctx.moveTo(-2, -6); ctx.lineTo(2, -6); ctx.lineTo(0, 4);
      ctx.fill();

      // 6. ANIMATED ARMS & HANDS
      const armSwing = hero.isMoving ? -Math.sin(hero.walkCycle) * 7 : 0;
      // Left arm
      ctx.fillStyle = "#1e40af";
      ctx.fillRect(-14, -8 - armSwing * 0.3, 5, 12);
      ctx.fillStyle = "#fed7aa"; // Skin hand
      ctx.beginPath();
      ctx.arc(-11.5, 6 - armSwing * 0.3, 3, 0, Math.PI * 2);
      ctx.fill();

      // Right arm (holding tablet/folder)
      ctx.fillStyle = "#2563eb";
      ctx.fillRect(9, -8 + armSwing * 0.3, 5, 12);
      ctx.fillStyle = "#06b6d4"; // Tech tablet / folder
      ctx.fillRect(11, 0 + armSwing * 0.3, 7, 9);
      ctx.fillStyle = "#fed7aa";
      ctx.beginPath();
      ctx.arc(11.5, 6 + armSwing * 0.3, 3, 0, Math.PI * 2);
      ctx.fill();

      // 7. HEAD & FACE
      ctx.fillStyle = "#fed7aa"; // Skin tone
      ctx.beginPath();
      ctx.arc(0, -18, 10, 0, Math.PI * 2);
      ctx.fill();

      // Hair
      ctx.fillStyle = "#331f0d"; // Dark brown hair
      ctx.beginPath();
      ctx.arc(0, -21, 10.5, Math.PI, Math.PI * 2);
      ctx.fill();
      ctx.fillRect(-10, -22, 20, 5);

      // Glasses & Eyes looking in direction
      ctx.strokeStyle = "#0f172a";
      ctx.lineWidth = 1.5;
      ctx.strokeRect(1, -21, 5, 5);
      ctx.strokeRect(-6, -21, 5, 5);
      ctx.beginPath();
      ctx.moveTo(-1, -19); ctx.lineTo(1, -19);
      ctx.stroke();

      // Smile
      ctx.strokeStyle = "#c2410c";
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.arc(0, -15, 3.5, 0.2, Math.PI - 0.2);
      ctx.stroke();

      ctx.restore();

      // 8. Floating Name Tag Badge Above Head
      const labelText = `👑 ${player.name || "Orquestrador"} • ${(player.score || 0).toLocaleString()} pts`;
      ctx.font = "bold 11px Outfit, sans-serif";
      const txtWidth = ctx.measureText(labelText).width;

      drawRoundRect(ctx, hero.x - txtWidth / 2 - 8, hero.y - 48, txtWidth + 16, 20, 10);
      ctx.fillStyle = "rgba(10, 19, 36, 0.92)";
      ctx.fill();
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.fillStyle = "#fff";
      ctx.textAlign = "center";
      ctx.fillText(labelText, hero.x, hero.y - 34);
    }

    function renderMinimap() {
      minimapCtx.clearRect(0, 0, 110, 80);
      const scaleX = 110 / WORLD_W;
      const scaleY = 80 / WORLD_H;

      // Base ground
      minimapCtx.fillStyle = "#070f1e";
      minimapCtx.fillRect(0, 0, 110, 80);

      // Lake in minimap
      minimapCtx.fillStyle = "#0284c7";
      minimapCtx.beginPath();
      minimapCtx.ellipse(680 * scaleX, 1180 * scaleY, 14, 7, 0, 0, Math.PI * 2);
      minimapCtx.fill();

      // Stations
      stations.forEach(st => {
        const isUnlocked = unlockedPhases.includes(st.block);
        const isCompleted = player.completedStations.includes(st.id);
        minimapCtx.fillStyle = isCompleted ? "#10b981" : isUnlocked ? st.color : "#475569";
        minimapCtx.beginPath();
        minimapCtx.arc(st.x * scaleX, st.y * scaleY, 4.5, 0, Math.PI * 2);
        minimapCtx.fill();
      });

      // Hero dot
      minimapCtx.fillStyle = "#fbbf24";
      minimapCtx.beginPath();
      minimapCtx.arc(hero.x * scaleX, hero.y * scaleY, 4, 0, Math.PI * 2);
      minimapCtx.fill();
    }

    /* Target Direction Arrow and Navigation Helper */
    function updateTargetBanner() {
      const nextSt = stations.find(s => unlockedPhases.includes(s.block) && !player.completedStations.includes(s.id));
      const banner = document.getElementById('direction-banner');
      const label = document.getElementById('target-label');
      const arrow = document.getElementById('target-arrow');

      if (!nextSt) {
        label.textContent = "Parabéns! Todas as fases liberadas foram concluídas!";
        arrow.textContent = "🏆";
        return;
      }

      label.textContent = `Vá até a ${nextSt.phaseLabel}: ${nextSt.name}`;
      const angle = Math.atan2(nextSt.y - hero.y, nextSt.x - hero.x);
      const deg = Math.round(angle * (180 / Math.PI));
      arrow.style.display = "inline-block";
      arrow.style.transform = `rotate(${deg}deg)`;
    }

    setInterval(updateTargetBanner, 300);

    /* Station Interaction */
    function checkNearbyStationInteraction() {
      stations.forEach(st => {
        const dist = Math.hypot(st.x - hero.x, st.y - hero.y);
        if (dist < st.radius + 45) {
          if (!unlockedPhases.includes(st.block)) {
            alert(`🔒 A ${st.phaseLabel} (${st.name}) ainda está bloqueada. O apresentador liberará ao final do bloco!`);
            playBeep(220, 'square', 0.2);
          } else if (player.completedStations.includes(st.id)) {
            alert(`✓ Você já concluiu todas as perguntas da ${st.phaseLabel}!`);
            playBeep(440, 'sine', 0.15);
          } else {
            openKahootChallenge(st);
          }
        }
      });
    }

    /* Kahoot Challenge Engine */
    let activeStation = null;
    let activeQuestions = [];
    let currentQIdx = 0;
    let qStartTime = 0;
    let qTimerInterval = null;
    const Q_MAX_SECONDS = 20;

    function openKahootChallenge(station) {
      activeStation = station;
      activeQuestions = rawQuestions.filter(q => q.block === station.block);
      currentQIdx = 0;

      document.getElementById('challenge-modal').style.display = 'flex';
      loadCurrentQuestion();
    }'''

code = engine_pattern.sub(new_engine_code, code)

# 4. Update the reset event listener in jogo.html
# Add GAME_RESET listener so that when admin triggers resetFullGame(), student view resets cleanly
reset_listener_code = '''
    // Listen for Full Game Reset from Admin Cockpit
    function handleGameReset() {
      player = {
        name: "",
        turma: "Quarta",
        score: 0,
        answeredQuestions: {},
        completedStations: []
      };
      localStorage.removeItem('kahoot_rpg_current_player');
      unlockedPhases = [1, 2, 3, 4, 5, 6]; // All phases unlocked on full reset
      
      const modalReg = document.getElementById('modal-register');
      if (modalReg) modalReg.style.display = 'flex';
      const modalChal = document.getElementById('challenge-modal');
      if (modalChal) modalChal.style.display = 'none';

      savePlayerState();
      updateTargetBanner();
      console.log('[Jogo] Jogo resetado com sucesso pelo Administrador!');
    }

    if (window.SyncService) {
      window.SyncService.onReset(() => handleGameReset());
    }

    if (channel) {
      const origOnMessage = channel.onmessage;
      channel.onmessage = (event) => {
        if (event.data && event.data.type === 'GAME_RESET') {
          handleGameReset();
        } else if (origOnMessage) {
          origOnMessage(event);
        }
      };
    }
'''

code = code.replace("window.addEventListener('DOMContentLoaded', () => {", reset_listener_code + "\n    window.addEventListener('DOMContentLoaded', () => {")

with open(jogo_path, "w", encoding="utf-8") as f:
    f.write(code)

print(f"Updated {jogo_path} ({len(code):,} bytes)")
