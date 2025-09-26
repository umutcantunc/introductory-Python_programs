print("""
*****************************************************
1)"Üçgen" ya da "Dörtgen" diyerek şeklinizi belirtin.
2)Kenarların uzunluklarını belirtin.
Şeklin özelliğini bulmuş olacaksınız.
*****************************************************
""")
sekil = input("Şekil tipini giriniz: ")
if sekil == "Üçgen":
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

elif sekil == "Dörtgen":
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