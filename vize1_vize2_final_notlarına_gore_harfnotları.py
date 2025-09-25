print("""
******************************************
Vize1 toplam notun %30'una etki edecek.
Vize2 toplam notun %30'una etki edecek.
Final toplam notun %40'ına etki edecek.
    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
******************************************
""")

vize1 = int(input("1.Vize Sonucunu girin:"))
vize2 = int(input("2.Vize Sonucunu girin:"))
final = int(input("Final sonucunu girin:"))
genel_not = ((vize1*30)/100) + ((vize2*30)/100) + ((final*40)/100)

print("Genel Notunuz:",genel_not)
if genel_not >= 90:
    print("Harf Notunuz: AA")
elif genel_not >= 85:
    print("Harf Notunuz: BA")
elif genel_not >= 80:
    print("Harf Notunuz: BB")
elif genel_not >= 75:
    print("Harf Notunuz: CB")
elif genel_not >= 70:
    print("Harf Notunuz: CC")
elif genel_not >= 65:
    print("Harf Notunuz: DC")
elif genel_not >= 60:
    print("Harf Notunuz: DD")
elif genel_not >= 55:
    print("Harf Notunuz: FD")
elif genel_not < 55:
    print("Harf Notunuz: FF")

