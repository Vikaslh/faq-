from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    """
    Extract text content from a PDF file.
    """
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content

# utils.py
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    """
    Extract text content from a PDF file.
    """
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content
