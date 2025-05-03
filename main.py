from flat import Bill, Flatemate
from reports import PdfReport

amount=float(input("enter the bill amount: "))
period=str(input("enter the period like:[month] [year]: "))
name1=input('enter the first person name')
name2=input('enter the second person name')
bill= Bill(amount=amount, period=period)
jhon= Flatemate(name=name1, day_in_house=20)
marry= Flatemate(name=name2, day_in_house=25)
print(f"{name1} has to pay",jhon.pays(bill=bill,flamate2=marry))
print(f"{name2} marry pays",marry.pays(bill=bill,flamate2=jhon))
file_name=f'{period}.pdf'
pdf= PdfReport(filename=file_name)
pdf.generate(flatemate1=jhon,flatemate2=marry,bill=bill)