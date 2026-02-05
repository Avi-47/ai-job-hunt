from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4

def export_resume_pdf(resume_text):
    file_path = "/mnt/data/AI_Tailored_Resume.pdf"

    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name="Header",
        parent=styles["Normal"],
        fontSize=12,
        spaceAfter=8,
        spaceBefore=10,
        leading=14
    ))

    styles.add(ParagraphStyle(
        name="Body",
        parent=styles["Normal"],
        fontSize=10,
        leading=13
    ))

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    elements = []

    for line in resume_text.split("\n"):

        clean = line.replace("&", "&amp;")

        if line.strip().isupper():   # section headers
            elements.append(Paragraph(f"<b>{clean}</b>", styles["Header"]))

        elif line.strip().startswith("•"):
            elements.append(Paragraph(clean, styles["Body"]))

        elif line.strip():
            elements.append(Paragraph(clean, styles["Body"]))

        else:
            elements.append(Spacer(1, 6))

    doc.build(elements)
    return file_path
