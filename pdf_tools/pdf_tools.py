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

def main():
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
        '13': ('PDF to WebP', pdf_to_webp.convert_pdf_to_webp)
    }

    print("Select an option:")
    for key, (description, _) in conversions.items():
        print(f"{key}. {description}")

    choice = input("Enter your choice (1-13): ")

    if choice in conversions:
        pdf_path = input("Enter the path to the PDF file: ")

        if choice in {'1', '2', '3', '4', '5', '6', '7','8','9','10','11','12','13'}:
            output_path = input("Enter the desired path for the output file: ")
            conversions[choice][1](pdf_path, output_path)
        else:
            output_dir = input("Enter the directory to save the images: ")
            conversions[choice][1](pdf_path, output_dir)
    else:
        print("Invalid choice. Please select 1-13.")

if __name__ == "__main__":
    main()
