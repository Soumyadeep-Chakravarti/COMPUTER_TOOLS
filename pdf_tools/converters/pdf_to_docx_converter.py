import fitz  # PyMuPDF
from docx import Document

def convert(pdf_path, docx_path):
    pdf_document = fitz.open(pdf_path)
    doc = Document()
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        doc.add_paragraph(text)
    
    doc.save(docx_path)
    print(f'PDF converted to Word document and saved as {docx_path}')
