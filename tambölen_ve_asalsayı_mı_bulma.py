print("""
******************************************************************
Girilen sayının tam bölenlerini ve asal olup olmadığını gösterir.
Tüm tam sayılar için proglanmıştır.
Çıkmak için "q" basınız.
*******************************************************************
""")
def tambolen(sayi):
    liste = [i for i in range(1,sayi+1) if sayi % i == 0]
    return liste

while True:
    sayi = input("Sayı giriniz: ")
    if sayi == "q":
        print("Program sonlandırıldı.")
        break
    if int(sayi) < 0:  #negatif sayılar için bir for döngüsünü -i şeklinde liste içinde gezdireceğiz.
        sayi = int(sayi)
        sayi = -sayi
        liste2 = [-i for i in tambolen(sayi)[::-1]] + tambolen(sayi) #küçükten büyüğe listelemek için listeyi tersten saydırıyoruz.
        print("Tam bölenler:",liste2)
        continue
    if int(sayi) == 0:
        print("0 hariç her sayıya bölünebilir.")
        continue
    else:
        sayi = int(sayi)
        print("Tam bölenler:",tambolen(sayi))
        if len(tambolen(sayi)) == 2:
            print("{} sayısı aynı zamanda asaldır.".format(sayi))
            continue