import logging
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Initialize lexers for all supported languages
LEXERS = {
    '.js': get_lexer_for_filename('example.js'),
    '.py': get_lexer_for_filename('example.py'),
    '.go': get_lexer_for_filename('example.go'),
    '.java': get_lexer_for_filename('example.java'),
    '.kt': get_lexer_for_filename('example.kt'),
    '.php': get_lexer_for_filename('example.php'),
    '.cs': get_lexer_for_filename('example.cs'),
    '.swift': get_lexer_for_filename('example.swift'),
    '.r': get_lexer_for_filename('example.r'),
    '.rb': get_lexer_for_filename('example.rb'),
    '.c': get_lexer_for_filename('example.c'),
    '.cpp': get_lexer_for_filename('example.cpp'),
    '.m': get_lexer_for_filename('example.m'),
    '.ts': get_lexer_for_filename('example.ts'),
    '.scala': get_lexer_for_filename('example.scala'),
    '.sql': get_lexer_for_filename('example.sql'),
    '.html': get_lexer_for_filename('example.html'),
    '.css': get_lexer_for_filename('example.css'),
    '.rs': get_lexer_for_filename('example.rs'),
    '.pl': get_lexer_for_filename('example.pl'),
}

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_to_html(input_file):
    try:
        logging.info(f"Starting HTML conversion for file: {input_file}")
        
        # Determine the file extension
        file_extension = input_file[input_file.rfind('.'):].lower()
        
        # Validate if the file extension is supported
        if file_extension not in LEXERS:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
        # Read the file line by line and process
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # Get the appropriate lexer
        lexer = LEXERS[file_extension]
        
        # Initialize formatter and highlight code
        formatter = HtmlFormatter(style='colorful')
        highlighted_code = ''
        
        for line in lines:
            highlighted_code += highlight(line, lexer, formatter)
        
        logging.info(f"HTML conversion completed for file: {input_file}")
        return highlighted_code
    
    except Exception as e:
        logging.error(f"Error during HTML conversion for file {input_file}: {e}")
        raise

def convert_to_pdf(input_file, output_file):
    try:
        logging.info(f"Starting PDF conversion for file: {input_file}")
        
        # Get syntax-highlighted HTML content
        highlighted_code = convert_to_html(input_file)
        
        # Generate PDF using reportlab
        c = canvas.Canvas(output_file, pagesize=letter)
        width, height = letter
        
        # Draw syntax-highlighted code as formatted text on PDF
        c.setFont("Courier", 10)
        lines = highlighted_code.splitlines()
        y = height - 40  # Initial y position, adjust margin as needed
        
        for line in lines:
            c.drawString(40, y, line)  # Draw each line of text at (40, y)
            y -= 12  # Adjust line spacing as needed
        
        c.save()
        
        logging.info(f"PDF conversion completed for file: {input_file}, saved as {output_file}")
    
    except Exception as e:
        logging.error(f"Error during PDF conversion for file {input_file}: {e}")
        raise

# Example usage
if __name__ == '__main__':
    input_file = 'example.py'  # Replace with your source code file path
    pdf_output = 'example.pdf'
    
    convert_to_pdf(input_file, pdf_output)
