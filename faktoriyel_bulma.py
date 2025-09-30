print("""
****************************
Faktöriyel Bulma Programı
Çıkmak için "q" ya basınız
****************************
""")

while True:
    sayi = input("Sayınızı giriniz:")
    if sayi == "q":
        print("Çıkış Yapılıyor")
        break
    else:
        sayi = int(sayi)
        if sayi < 0 :
            print("0 veya 0'dan büyük değerler giriniz")
            continue
        faktoriyel = 1
        for i in range(2,sayi+1):
            faktoriyel *= i
    print("{}! = {}".format(sayi, faktoriyel))
