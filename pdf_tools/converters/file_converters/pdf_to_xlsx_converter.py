import logging
import fitz
import pandas as pd

def convert(pdf_path, xlsx_path):
    try:
        logging.info(f"Starting PDF to Excel conversion: {pdf_path} to {xlsx_path}")
        pdf_document = fitz.open(pdf_path)
        df_list = []
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text("text") # type: ignore
            df = pd.DataFrame([text.split('\n')])
            df_list.append(df)

            logging.info(f"Added page {page_num + 1} to the DataFrame")

        final_df = pd.concat(df_list, ignore_index=True)
        final_df.to_excel(xlsx_path, index=False, header=False)
        logging.info(f"PDF to Excel conversion completed: {xlsx_path}")
    except Exception as e:
        logging.error(f"Error converting PDF to Excel: {e}")
    finally:
        if 'pdf_document' in locals():
            pdf_document.close()
