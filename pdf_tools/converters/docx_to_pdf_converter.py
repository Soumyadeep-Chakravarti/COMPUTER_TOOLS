from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert(docx_path, pdf_path):
    doc = Document(docx_path)
    pdf = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    for para in doc.paragraphs:
        text = para.text
        
        text_object = pdf.beginText()
        text_object.setTextOrigin(40, height - 40)
        text_object.setFont("Helvetica", 12)
        text_object.textLines(text)
        
        pdf.drawText(text_object)
        pdf.showPage()
    
    pdf.save()
    print(f'Word document converted to PDF and saved as {pdf_path}')
