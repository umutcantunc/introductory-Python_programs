print("""
****************************
ATM PROGRAMINA HOŞ GELDİNİZ

BAKİYE SORMA İÇİN 1
PARA YATIRMA İÇİN 2
PARA ÇEKMEK İÇİN 3
ÇIKIŞ YAPMAK İÇİN q
****************************
""")
bakiye = 1000
while True:
    islem = input("İşleminizi seçiniz:")

    if islem == "q":
        print("Yine bekleriz...")
        break
    elif islem == "1":
        print("Bakiyeniz {} TL".format(bakiye))
    elif islem == "2":
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz:"))
        bakiye += miktar
        print("Paranız yatırılıyor...")
        print("Yeni bakiyeniz {} TL".format(bakiye))
    elif islem == "3":
        miktar = int(input("Çekmek istediğiniz miktarı giriniz:"))
        if bakiye < miktar:
            print("En fazla bakiyeniz ({}TL) kadar çekebilirsiniz".format(bakiye))
            continue
        bakiye -= miktar
        print("Paranız çekiliyor...")
        print("Yeni bakiyeniz {} TL".format(bakiye))
    else:
        print("Geçersiz işlem girdiniz")
