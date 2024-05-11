"""
   Yarıçapı verilen bir dairenin
   alan ve çevresini hesaplayınız. ( pi:3.14)
"""

yaricap=float(input ("yari cap: "))

pi=3.14

alan=pi*(yaricap**2)
cevre=2*pi*yaricap

print("Alan: " , alan)
print("Çevre: " , cevre)

print("Alan: "+ str(alan)+ " Çevre: "+ str(cevre))