from converters import pdf_to_ppt_converter, ppt_to_pdf_converter, pdf_to_docx_converter, docx_to_pdf_converter, pdf_to_xlsx_converter, xlsx_to_pdf_converter

def main():
    print("Select an option:")
    print("1. Convert PDF to PowerPoint")
    print("2. Convert PowerPoint to PDF")
    print("3. Convert PDF to Word document")
    print("4. Convert Word document to PDF")
    print("5. Convert PDF to Excel (XLSX)")
    print("6. Convert Excel (XLSX) to PDF")
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        pdf_path = input("Enter the path to the PDF file: ")
        ppt_path = input("Enter the desired path for the PowerPoint file: ")
        pdf_to_ppt_converter.convert(pdf_path, ppt_path)
    elif choice == '2':
        ppt_path = input("Enter the path to the PowerPoint file: ")
        pdf_path = input("Enter the desired path for the PDF file: ")
        ppt_to_pdf_converter.convert(ppt_path, pdf_path)
    elif choice == '3':
        pdf_path = input("Enter the path to the PDF file: ")
        docx_path = input("Enter the desired path for the Word document file: ")
        pdf_to_docx_converter.convert(pdf_path, docx_path)
    elif choice == '4':
        docx_path = input("Enter the path to the Word document file: ")
        pdf_path = input("Enter the desired path for the PDF file: ")
        docx_to_pdf_converter.convert(docx_path, pdf_path)
    elif choice == '5':
        pdf_path = input("Enter the path to the PDF file: ")
        xlsx_path = input("Enter the desired path for the Excel (XLSX) file: ")
        pdf_to_xlsx_converter.convert(pdf_path, xlsx_path)
    elif choice == '6':
        xlsx_path = input("Enter the path to the Excel (XLSX) file: ")
        pdf_path = input("Enter the desired path for the PDF file: ")
        xlsx_to_pdf_converter.convert(xlsx_path, pdf_path)
    else:
        print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
