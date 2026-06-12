from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_report_pdf(report_text: str,
                        output_path: str = "research_report.pdf"):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "AI Research Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # Split report into lines
    lines = report_text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Headings
        if (
            "Executive Summary" in line
            or "Key Highlights" in line
            or "Conclusion" in line
            or "Sources" in line
        ):
            elements.append(
                Paragraph(
                    f"<b>{line}</b>",
                    styles["Heading2"]
                )
            )

        # Bullet Points
        elif line.startswith("-") or line.startswith("•"):
            elements.append(
                Paragraph(
                    f"• {line.replace('•','').replace('-','').strip()}",
                    styles["BodyText"]
                )
            )

        else:
            elements.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

        elements.append(Spacer(1, 6))

    doc.build(elements)

    return output_path

