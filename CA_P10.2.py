"""
We have three categories to check. If the sum of divisors is greater than a number, the number is
abundant. If the sum of divisors is less than a number, the number is deficient. Otherwise, it must
be perfect design control structure for this problem statement

#Nint=28 # Number to be validated 
#Div=1    #Divisor
#while Div<Nint:
#   if Nint % Div==0:
#        print(Div) # Suit1
#Div=Div+1  # Suit 2
"""
Nint= int(input())
Div=1
s=0
while Div<Nint:
    if Nint% Div==0:
        s+=Div
    Div= Div+1

if s>Nint:
    print("The number", Nint, "is abundant")
elif s<Nint:
    print("The number", Nint, "is deficient")
else:
    print("The number", Nint, "is perfect")