print("""
*********************************************************************************************************
"x" basamaklı bir sayının tüm basamaklarındaki rakamların x'inci kuvvetlerinin toplamı
kendisine eşit olan sayılara " Armstrong sayısı" denir.
 Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
*********************************************************************************************************

""")

sayi = input("Sayınızı giriniz:")
liste = [*sayi]
toplam = 0                       #while olacaksa basamak degiskeni de eklenmeli
for i in liste:                  #Burada while döngüsü ile yapmak için sayıyı devamlı %(mod) 10  ve // 10 kullanabiliriz.while (sayi > 0):
    toplam = toplam + int(i) ** len(liste)
if toplam == int(sayi):
    print("{} Armstrong sayısıdır.".format(sayi))
    print("Toplam sonucu:", toplam)
else:
    print("{} Armstrong sayısı değildir.".format(sayi))
    print("Toplam sonucu:", toplam)

