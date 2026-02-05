import os
import requests
from io import BytesIO
from PIL import Image
import pytesseract
from pypdf import PdfReader
from docx import Document
import easyocr
import numpy as np


# ---------- Core Readers ----------

def read_pdf_bytes(data):
    reader = PdfReader(BytesIO(data))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def read_docx_bytes(data):
    file = BytesIO(data)
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)



reader = easyocr.Reader(['en'], gpu=False)

def read_image_bytes(data):
    results = reader.readtext(data)
    return " ".join([text for _, text, _ in results])

def image_to_pdf_bytes(image_bytes):
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    pdf_bytes = BytesIO()
    img.save(pdf_bytes, format="PDF")
    return pdf_bytes.getvalue()


# ---------- Main Universal Loader ----------

def extract_text(source):
    """
    source can be:
    - Streamlit uploaded file
    - local file path
    - URL (PDF)
    """

    # 🌐 PDF from link
    if isinstance(source, str) and source.startswith("http"):
        response = requests.get(source)
        return read_pdf_bytes(response.content)

    # 📁 Local file path
    if isinstance(source, str):
        with open(source, "rb") as f:
            data = f.read()
        ext = os.path.splitext(source)[1].lower()

    # 📤 Streamlit upload
    else:
        data = source.read()
        ext = os.path.splitext(source.name)[1].lower()

    # ---------- Dispatch ----------
    if ext == ".pdf":
        return read_pdf_bytes(data)

    if ext == ".docx":
        return read_docx_bytes(data)

    if ext == ".txt":
        return data.decode("utf-8")

    if ext in [".png", ".jpg", ".jpeg"]:
        pdf_data = image_to_pdf_bytes(data)
        return read_pdf_bytes(pdf_data)
    raise ValueError("Unsupported file format")
