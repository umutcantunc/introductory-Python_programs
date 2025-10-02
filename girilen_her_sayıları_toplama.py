toplam = 0
sayac = 0
liste = []
while True:
    sayi = input("Sayı giriniz:")
    if sayi == "q":
        break
    toplam = toplam + int(sayi)
    sayac += 1
    liste.append(sayi)
print("Toplam sonucu:", toplam)
print("Girilen sayılar:",liste)
print("Girilen sayı adeti:",sayac)
