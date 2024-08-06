import fitz  # PyMuPDF
from PIL import Image

def create_pdf_with_images(image_paths, output_pdf_path):
    """
    Create a PDF document from a list of image file paths.

    :param image_paths: List of paths to image files.
    :param output_pdf_path: Path where the output PDF should be saved.
    """
    # Create a new PDF document
    pdf_document = fitz.open()
    
    for image_path in image_paths:
        # Open the image using PIL
        image = Image.open(image_path)
        
        # Get image dimensions
        image_width, image_height = image.size
        
        # Create a new PDF page with the same dimensions as the image
        page = pdf_document.new_page(width=image_width, height=image_height)
        
        # Insert the image into the page
        page.insert_image(page.rect, filename=image_path)
    
    # Save the PDF to a file
    pdf_document.save(output_pdf_path)
    pdf_document.close()
