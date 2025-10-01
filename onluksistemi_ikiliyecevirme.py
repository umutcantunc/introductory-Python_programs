sayi = int(input("Sayınızı girin:"))
binary = ""
if sayi == 0:
    print("İkilik tabandaki karşılığı:",sayi)
else:
    while True:
        if sayi < 0:
            sayi = int(input("Sayınız negatif olamaz tekrar sayı girin:"))
            if sayi == 0:
                print(print("İkilik tabandaki karşılığı:",sayi))
                break
        if sayi == 0:
            print("İkilik tabandaki karşılığı:", binary)
            break
        binary = str(sayi%2) + binary
        sayi = int(sayi/2)
