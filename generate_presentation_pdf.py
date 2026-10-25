import os
import sys
import time
from playwright.sync_api import sync_playwright
import fitz  # PyMuPDF

def generate_pdf():
    html_path = os.path.abspath('index.html')
    file_url = 'file:///' + html_path.replace('\\', '/')
    output_pdf = 'Seminario_5_Ecossistemas_de_Inovacao_PPGPIT_UNIFESP.pdf'

    print(f'Iniciando geração do PDF a partir de {file_url}...')
    t0 = time.time()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel='chrome')
        # Viewport de alta definição (1920x1080 a 1.5x scale factor para nitidez máxima de fontes e gráficos)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1.5)
        page.goto(file_url, wait_until='networkidle')
        page.wait_for_timeout(1000)

        # Ocultar botões interativos de topo e botões de navegação para um PDF limpo e formal
        page.evaluate("""
            const hideSelectors = [
                '.deck-btn', '#btn-fs', '#btn-notes', '#btn-grid', '#btn-rpg', '#deck-timer',
                '.nav-arrow-btn', '#drawer-notes', '#drawer-grid', '#modal-rpg', '#toast-container'
            ];
            hideSelectors.forEach(sel => {
                document.querySelectorAll(sel).forEach(el => el.style.display = 'none');
            });

            // Desativar transições CSS para renderização estática instantânea
            const style = document.createElement('style');
            style.textContent = `
                * { transition: none !important; animation: none !important; }
                .slide { transition: none !important; }
            `;
            document.head.appendChild(style);
        """)

        # Obter número total de slides
        total_slides = page.evaluate("totalSlides || 47")
        print(f"Total de slides a capturar: {total_slides}")

        pdf_doc = fitz.open()

        for s in range(1, total_slides + 1):
            page.evaluate(f"showSlide({s})")
            # Pequena pausa para garantir renderização de canvas (radar) e diagramas
            page.wait_for_timeout(150)
            
            img_bytes = page.screenshot(type='png')
            img_doc = fitz.open(stream=img_bytes, filetype='png')
            page_pdf_bytes = img_doc.convert_to_pdf()
            slide_pdf = fitz.open('pdf', page_pdf_bytes)
            pdf_doc.insert_pdf(slide_pdf)
            
            if s % 5 == 0 or s == total_slides:
                print(f"Progresso: Slide {s}/{total_slides} processado...")

        # Configurar metadados do documento PDF
        pdf_doc.set_metadata({
            'title': 'Seminário 5: Ecossistemas de Inovação & PIT SJC',
            'author': 'UNIFESP PPG-PIT - Gestão Estratégica da Inovação',
            'subject': 'Apresentação Completa - Mestrado em Inovação Tecnológica UNIFESP',
            'keywords': 'Ecossistemas de Inovação, PIT SJC, Hélice Quíntupla, Ron Adner, James Moore, UNIFESP',
            'creator': 'UNIFESP PPG-PIT / Google Antigravity',
            'producer': 'PyMuPDF + Playwright'
        })

        pdf_doc.save(output_pdf, deflate=True)
        pdf_doc.close()
        browser.close()

    elapsed = time.time() - t0
    file_size_mb = os.path.getsize(output_pdf) / (1024 * 1024)
    print(f"\nPDF gerado com sucesso em {elapsed:.1f}s!")
    print(f"Arquivo: {output_pdf} ({file_size_mb:.2f} MB - {total_slides} páginas)")

if __name__ == '__main__':
    generate_pdf()
