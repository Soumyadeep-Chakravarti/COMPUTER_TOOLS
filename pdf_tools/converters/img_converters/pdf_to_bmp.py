import fitz
import os
import logging
from PIL import Image
import io

def convert_pdf_to_bmp(pdf_path, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        pdf_document = fitz.open(pdf_path)
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            pix = page.get_pixmap() # type: ignore
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            image_filename = os.path.join(output_dir, f'image_{page_number+1}.bmp')
            image.save(image_filename, format='BMP')
            logging.info(f'Saved {image_filename}')
            del image

        logging.info(f"Extracted {len(pdf_document)} BMP images from the PDF.")
    except Exception as e:
        logging.error(f"Error processing PDF to BMP: {e}")
    finally:
        if 'pdf_document' in locals():
            pdf_document.close()
