print("""
**************************************
ÜÇ SAYININ EN BÜYÜĞÜNÜ BULMA PROGRAMI
**************************************
""")
a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))
c = int(input("Üçüncü Sayı:"))

if a >= b and a >= c:
    print("En büyük sayı:",a)
elif b >= a and b >= c:
    print("En büyük sayı:",b)
elif c >= a and c >= b:
    print("En büyük sayı:",c)


