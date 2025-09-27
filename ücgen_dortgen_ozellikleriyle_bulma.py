print("""
*****************************************************
1)"Üçgen","üçgen","3" ya da "Dörtgen","dörtgen","4" diyerek şeklinizi belirtin.
2)Kenarların uzunluklarını belirtin.
Şeklin özelliğini bulmuş olacaksınız.
*****************************************************
""")
sekil = input("Şekil tipini giriniz: ")
if sekil == "Üçgen" or sekil == "üçgen" or sekil == "3":
    a = int(input("1.kenarı giriniz:"))
    b = int(input("2.kenarı giriniz:"))
    c = int(input("3.kenarı giriniz:"))
    if a + b > c and abs(a - b) < c:
        if a == b == c:
            print("Eşkenar Üçgen")
        elif a == b and a != c or a == c and a != b or b == c and b != a:
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen belirtmiyor.")

elif sekil == "Dörtgen" or sekil == "dörtgen" or sekil == "4":
    a = int(input("1.kenarı giriniz:"))
    b = int(input("2.kenarı giriniz:"))
    c = int(input("3.kenarı giriniz:"))
    d = int(input("4.kenarı giriniz:"))
    if a==b==c==d:
        print("Kare")
    else:
        print("Sıradan dörtgen")
else:
    print("Hatalı Şekil")