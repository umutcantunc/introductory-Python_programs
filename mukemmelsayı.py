sayi = int(input("Sayınızı girin:"))
i = 0
bolenler_toplamı = 0
bolenler = []
while i <= sayi:
    i += 1
    if sayi % i == 0:
        bolenler_toplamı = bolenler_toplamı + i
        bolenler.append(i)

if sayi == bolenler_toplamı - sayi:
    print("{} mükemmel bir sayıdır.".format(sayi))
    print("Sayının bölenleri:", bolenler)
else:
    print("{} mükemmel bir sayı değildir.".format(sayi))
    print("Sayının bölenleri:", bolenler)

