from fpdf import FPDF;

name = input("Name: ")
pdf = FPDF();
pdf.add_page();
pdf.set_font("helvetica", "B", 40);
pdf.cell(0, pdf.eph/8, "CS50 Shirtficate", align='c');
pdf.ln(10)
pdf.image("shirtificate.png", x=0, y=pdf.eph/4);
pdf.set_font("helvetica", "B", 25);
pdf.set_text_color(255, 255, 255);
pdf.cell(0, 250, f'{name} took CS50', align='c');
pdf.output("shirtificate.pdf")