print("""
*********************************************************
                   SAYI TAHMİN OYUNU
     1 ile istenilen sayı arasındaki sayıyı tahmin edin
     Aralığınız arttıkça tahmin hakkınız da artacaktır.
*********************************************************
""")
import random
import time
import math

sinir_sayi = int(input("1 ile hangi sayı arasında bir sayı belirlensin?:"))

rastgele_sayi = random.randint(1,sinir_sayi)

tahmin_hakkı = int(math.log2(sinir_sayi)) #binary search baz alınarak bir tahmin hakkı sayısı olusturmak ıcın
sayac = tahmin_hakkı + 1 #kacıncı tahminimiz oldugunu belırtmek ıcın (bunu asagıda kullanacagız)

print("Bu aralıktaki bir sayı seçiliyor...")
time.sleep(1)
print("Sayınız seçildi!","Tahmin Hakkınız:",tahmin_hakkı)
time.sleep(1)

while True:
    tahmin = int(input("Tahminizi giriniz:"))

    if tahmin < rastgele_sayi:
        print("Kontrol ediliyor...")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Daha yüksek bir sayı söyleyin","(Kalan tahmin hakkınız:{})".format(tahmin_hakkı))
    elif tahmin > rastgele_sayi:
        print("Kontrol ediliyor...")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Daha düşük bir sayı söyleyin","(Kalan tahmin hakkınız:{})".format(tahmin_hakkı))
    else:
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Tebrikler! Sayımız:",rastgele_sayi)
        print("({}.tahmininizde bildiniz)".format(sayac - tahmin_hakkı))
        break

    if tahmin_hakkı == 0:
        print("Tahmin hakkınız bitti!")
        print("Tutulan sayı:",rastgele_sayi)
        break