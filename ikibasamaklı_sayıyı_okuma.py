birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
def okunus(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10

    return onlar[ikinci] + " " + birler[birinci]
sayi = int(input("İki basamaklı doğal sayı giriniz:"))

print(okunus(sayi))