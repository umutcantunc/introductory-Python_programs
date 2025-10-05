print("""
**********************************************
İki sayı girerek sayı aralığını belirleyip 
aralıktaki mükemmel sayıları bulabilirsiniz.
**********************************************
""")
def mukemmelsayi(sayi):
    toplam = 0
    for i in range(1,sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

while True:
    s1 = input("1.aralığı giriniz:")
    if int(s1) <=0:
        print("Sadece pozitif tam sayı giriniz.")
        continue
    if s1 == "q":
        print("Program sonlandırıldı.")
        break

    s2 = input("2.aralığı giriniz:")
    if int(s2) <=0:
        print("Sadece pozitif tam sayı giriniz.")
        continue
    if s2 == "q":
        print("Program sonlandırıldı.")
        break

    else:
        s1,s2 = int(s1), int(s2)
        sayac = 1
        if s1 > s2:
            s1,s2 = s2,s1
            for sayi in range(s1, s2+1):
                if mukemmelsayi(sayi):
                    print("{}.Mükemmel sayı:".format(sayac),sayi)
                    sayac += 1
        else:
            for sayi in range(s1, s2):
                if mukemmelsayi(sayi):
                    print("{}.Mükemmel sayı:".format(sayac),sayi)
                    sayac += 1