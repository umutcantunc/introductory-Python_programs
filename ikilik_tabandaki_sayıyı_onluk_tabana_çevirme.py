import math

binary = int(input("İkilik tabandaki(0 ve 1'lerden oluşan) sayıyı giriniz: "))
basamak = int(math.log(binary,10)) + 1
toplam = 0
i = 0
while i <= basamak:
    for j in range(1,basamak+2):
        toplam += ((binary % (10 ** j))//10**(j-1)) * (2**i)
        i += 1

print("Onluk tabanda karşılığı:",toplam)