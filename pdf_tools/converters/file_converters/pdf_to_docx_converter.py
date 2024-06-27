import logging
import fitz
from docx import Document

def convert(pdf_path, docx_path):
    try:
        logging.info(f"Starting PDF to Word conversion: {pdf_path} to {docx_path}")
        pdf_document = fitz.open(pdf_path)
        document = Document()
        
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            text = page.get_text("text") # type: ignore
            document.add_paragraph(text)

            logging.info(f"Added page {page_number + 1} to the Word document")

        document.save(docx_path)
        logging.info(f"PDF to Word conversion completed: {docx_path}")
    except Exception as e:
        logging.error(f"Error converting PDF to Word: {e}")
    finally:
        if 'pdf_document' in locals():
            pdf_document.close()
