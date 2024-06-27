import logging
import fitz
import pandas as pd

def convert(xlsx_path, pdf_path):
    try:
        logging.info(f"Starting Excel to PDF conversion: {xlsx_path} to {pdf_path}")
        df = pd.read_excel(xlsx_path, header=None)
        pdf_document = fitz.open()

        for index, row in df.iterrows():
            page = pdf_document.new_page() # type: ignore
            text = ' '.join(row.dropna().astype(str).tolist())
            page.insert_text((72, 72), text)

            logging.info(f"Added row {index + 1} to PDF") # type: ignore

        pdf_document.save(pdf_path)
        logging.info(f"Excel to PDF conversion completed: {pdf_path}")
    except Exception as e:
        logging.error(f"Error converting Excel to PDF: {e}")
    finally:
        if 'pdf_document' in locals():
            pdf_document.close()

# Example usage
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    xlsx_path = 'example.xlsx'  # Replace with your Excel file path
    pdf_path = 'output.pdf'     # Replace with your desired PDF output file path
    
    convert(xlsx_path, pdf_path)
