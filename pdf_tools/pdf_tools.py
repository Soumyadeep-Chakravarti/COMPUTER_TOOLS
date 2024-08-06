from converters.file_converters import (
    pdf_to_ppt_converter,
    ppt_to_pdf_converter,
    pdf_to_docx_converter,
    docx_to_pdf_converter,
    pdf_to_xlsx_converter,
    xlsx_to_pdf_converter,
    code_to_pdf_converter,
)
from converters.img_converters import (
    pdf_to_bmp,
    pdf_to_gif,
    pdf_to_jpeg,
    pdf_to_png,
    pdf_to_tiff,
    pdf_to_webp,
    imgs_to_pdf
)
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pdf_conversion.log'),
        logging.StreamHandler()
    ]
)

conversions = {
    '1': ('PDF to PowerPoint', pdf_to_ppt_converter.convert),
    '2': ('PowerPoint to PDF', ppt_to_pdf_converter.convert),
    '3': ('PDF to Word document', pdf_to_docx_converter.convert),
    '4': ('Word document to PDF', docx_to_pdf_converter.convert),
    '5': ('PDF to Excel (XLSX)', pdf_to_xlsx_converter.convert),
    '6': ('Excel (XLSX) to PDF', xlsx_to_pdf_converter.convert),
    '7': ('Source Code to PDF', code_to_pdf_converter.convert_to_pdf),
    '8': ('PDF to JPEG', pdf_to_jpeg.convert_pdf_to_jpeg),
    '9': ('PDF to PNG', pdf_to_png.convert_pdf_to_png),
    '10': ('PDF to GIF', pdf_to_gif.convert_pdf_to_gif),
    '11': ('PDF to TIFF', pdf_to_tiff.convert_pdf_to_tiff),
    '12': ('PDF to BMP', pdf_to_bmp.convert_pdf_to_bmp),
    '13': ('PDF to WebP', pdf_to_webp.convert_pdf_to_webp),
    '14': ("Create PDF from Images", imgs_to_pdf.create_pdf_with_images),
}

def perform_conversion(choice, pdf_path, output_path):
    if choice in conversions:
        try:
            conversion_func = conversions[choice][1]
            conversion_func(pdf_path, output_path)
            logging.info(f"Conversion for choice {choice} completed.")
            return True, "Conversion completed successfully!"
        except Exception as e:
            logging.error(f"Conversion failed: {e}")
            return False, f"An error occurred during conversion: {e}"
    else:
        return False, "Invalid conversion choice."
