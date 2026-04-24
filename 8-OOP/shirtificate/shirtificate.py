from fpdf import FPDF


def main():
    name = input("What is your name? ")

    pdf = FPDF()
    pdf = set_up(pdf)
    add_image_title_name(pdf, name)
    pdf.output("shirtificate.pdf")


def set_up(pdf):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    return pdf


def add_image_title_name(pdf, name):
    pdf.add_page()

    pdf.image("shirtificate.png", 0, 50, 0)

    pdf.set_font(
        "Helvetica",
        style="B",
        size=28,
    )
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "CS50 Shirtficate", border=1, align="C")

    pdf.ln(90)

    pdf.set_font(
        "Helvetica",
        style="B",
        size=16,
    )
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 0, f"{name} took CS50", align="C")


main()
