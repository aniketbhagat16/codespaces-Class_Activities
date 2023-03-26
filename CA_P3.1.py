"""Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)"""

c=input("Which Arithetic operation you want to get? ")
a=int(input("Enter no. 1 "))
b=int(input("Enter no. 2 "))
if c=="add" or c=="Add" or c=="ADD" or c=="plus" or c=="Plus" :
    print(a+b)
elif c=="subtract" or c=="Subtract" or c=="SUBTRACT" or c=="minus" or c=="Minus":
    print(a-b)   
elif c=="multiply" or c=="Multiply" or c=="MULTIPLY" or c=="Multiplication" or c=="multiplication":
    print(a*b)
elif c=="divide" or c=="Divide" or c=="DIVIDE" or c=="Division" or c=="division":
    print(a/b)
elif c=="power" or c=="Power" or c=="POWER":
    print(a**b)
elif c=="floor division" or c=="Floor Division" or c=="Floor division" or c=="FLOOR DIVISION":
    print(a//b)
elif c=="remainder" or c=="Remainder" or c=="REMAINDER":
    print(a%b)
else:
    print("Invalid Arithmetic Operation")