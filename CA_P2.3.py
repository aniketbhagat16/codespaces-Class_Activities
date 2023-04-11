"""Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)"""

mgn = float(input("Enter magnitude of Earthquake: "))

if mgn<=0:
    print("No Earthquake")
elif 0<mgn<2:
    print("Micro Earthquake")
elif 2<=mgn<3:
    print("Very Minor Earthquake")
elif 3<=mgn<4:
    print("Minor Earthquake")
elif 4<=mgn<5:
    print("Light Earthquake")
elif 5<=mgn<6:
    print("Moderate Earthquake")
elif 6<=mgn<7:
    print("Strong Earthquake")
elif 7<=mgn<8:
    print("Major Earthquake")
else:
    print("Great Earthquake")