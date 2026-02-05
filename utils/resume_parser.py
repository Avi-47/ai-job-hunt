import pdfplumber
from docx import Document
from PIL import Image
import pytesseract
import io

def read_resume(file):
    name = file.name.lower()

    if name.endswith(".pdf"):
        return read_pdf(file)

    elif name.endswith(".docx"):
        return read_docx(file)

    elif name.endswith(".txt"):
        return file.read().decode("utf-8")

    elif name.endswith((".png", ".jpg", ".jpeg")):
        return read_image(file)

    else:
        raise ValueError("Unsupported file format")


def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def read_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)


def read_image(file):
    img = Image.open(file)
    return pytesseract.image_to_string(img)
