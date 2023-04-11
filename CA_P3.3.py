"""Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)"""

magnitude = float(input("Enter magnitude of Earthquake: "))
def Earthquake_Impact(magnitude):
    
    if magnitude<=0:
        return "No Earthquake"
    elif 0<magnitude<2:
        return "Micro Earthquake"
    elif 2<=magnitude<3:
        return "Very Minor Earthquake"
    elif 3<=magnitude<4:
        return "Minor Earthquake"
    elif 4<=magnitude<5:
        return "Light Earthquake"
    elif 5<=magnitude<6:
        return "Moderate Earthquake"
    elif 6<=magnitude<7:
        return "Strong Earthquake"
    elif 7<=magnitude<8:
        return "Major Earthquake"
    else:
        return "Great Earthquake"
print(Earthquake_Impact(magnitude))