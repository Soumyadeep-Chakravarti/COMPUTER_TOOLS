import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert(xlsx_path, pdf_path):
    # Read Excel file into a dataframe
    df = pd.read_excel(xlsx_path, header=None)
    
    pdf = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    for index, row in df.iterrows():
        text = ' '.join(map(str, row))
        
        text_object = pdf.beginText()
        text_object.setTextOrigin(40, height - 40)
        text_object.setFont("Helvetica", 12)
        text_object.textLines(text)
        
        pdf.drawText(text_object)
        pdf.showPage()
    
    pdf.save()
    print(f'Excel (XLSX) converted to PDF and saved as {pdf_path}')
