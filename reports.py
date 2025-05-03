import webbrowser,os

from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF files that containes data about the flatemates such as
    due amount and period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatemate1,flatemate2,bill):
        flatemate1_pay=str(round(flatemate1.pays(bill=bill,flamate2=flatemate2),2))
        flatemate2_pay=str(round(flatemate2.pays(bill=bill, flamate2=flatemate1), 2))
        pdf = FPDF(orientation='P', format='A4', unit='pt')
        pdf.add_page()
        pdf.image("files/house.png",w=30,h=30)

        pdf.set_font(family='Arial', size=20, style='B')
        # insert title
        pdf.cell(w=0, h=80, txt='Flat Mate Bill', border=1, align='C', ln=1)
        # insert period lable and value
        pdf.set_font(family='Arial', size=10,style='B')
        pdf.cell(w=100, h=20, txt='period:', border=1)
        pdf.cell(w=100, h=20, txt=bill.period, border=1, ln=1)

        # insert name  and bill of each faltmate
        pdf.cell(w=100, h=20, txt=flatemate1.name, border=1)
        pdf.cell(w=100, h=20, txt=flatemate1_pay, border=1, ln=1)

        pdf.cell(w=100, h=20, txt=flatemate2.name, border=1)
        pdf.cell(w=100, h=20, txt=flatemate2_pay, border=1, ln=1)

        # chane directory
        os.chdir('files')
        pdf.output(self.filename)
        webbrowser.open(self.filename)
