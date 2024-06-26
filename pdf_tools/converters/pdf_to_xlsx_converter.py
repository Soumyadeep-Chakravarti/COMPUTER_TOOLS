import fitz  # PyMuPDF
import pandas as pd

def convert(pdf_path, xlsx_path):
    pdf_document = fitz.open(pdf_path)
    df_list = []
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text") # type: ignore
        df = pd.DataFrame([text.split('\n')])
        df_list.append(df)
    
    # Concatenate all dataframes into a single dataframe
    final_df = pd.concat(df_list, ignore_index=True)
    
    # Save dataframe to Excel
    final_df.to_excel(xlsx_path, index=False, header=False)
    print(f'PDF converted to Excel (XLSX) and saved as {xlsx_path}')


