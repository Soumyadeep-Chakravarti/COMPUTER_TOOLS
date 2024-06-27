import logging
from docx import Document
import fitz

def convert(docx_path, pdf_path):
    try:
        logging.info(f"Starting Word to PDF conversion: {docx_path} to {pdf_path}")
        document = Document(docx_path)
        pdf_document = fitz.open()

        for paragraph in document.paragraphs:
            text = paragraph.text
            page = pdf_document.new_page() # type: ignore
            page.insert_text((72, 72), text)

            logging.info(f"Added paragraph to PDF")

        pdf_document.save(pdf_path)
        logging.info(f"Word to PDF conversion completed: {pdf_path}")
    except Exception as e:
        logging.error(f"Error converting Word to PDF: {e}")
    finally:
        if 'pdf_document' in locals():
            pdf_document.close()
