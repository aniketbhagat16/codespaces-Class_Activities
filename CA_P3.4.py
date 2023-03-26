"""Factor:  Calculate temperature that a person feels because of the wind (Python3)"""

T=float(input("Enter temperature in °C: "))
w=float(input("Enter wind speed in Km/h: "))
output= 13.12 + 0.6215*T - 11.37*(w**0.16) + 0.3965*T*(w**0.16)
print(round(output,2),"°C")