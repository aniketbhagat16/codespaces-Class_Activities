"""Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3)"""

a=float(input("Enter distance in Kilometers: "))
def km_miles(a):
    conversion=a/1.069
    return conversion
print(km_miles(a),"miles")
def km_meter(a):
    conversion=a*1000
    return conversion
print(km_meter(a),"meters")
b=float(input("Enter the weight of oil in Kilograms: "))
def kg_gram(b):
    conversion=b*1000
    return conversion
print(kg_gram(b),"grams")
def kg_litre(b):
    conversion=b*1.1364
    return conversion
print(kg_litre(b),"litres")