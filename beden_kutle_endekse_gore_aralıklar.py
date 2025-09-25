print("""
***************************************************
BEDEN KÜTLE ENDEKSİNİZE GÖRE ARALIĞINIZI BULUN
 BKİ 18.5'un altındaysa -------> Zayıf
 BKİ 18.5 ile 25 arasındaysa ------> Normal
 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
 BKİ 30'un üstündeyse -------------> Obez
***************************************************
""")
boy = int(input("Boyunuzu giriniz(cm):"))
kilo = int(input("Kilonuzu giriniz:"))
bki = kilo/((boy/100)**2)

if bki < 18.5:
    print("Zayıf")
elif bki >= 18.5 and bki <= 25:
    print("Normal")
elif bki >= 25 and bki <= 30:
    print("Fazla Kilolu")
elif bki >= 30:
    print("Obez")
print("Bki değeriniz:",bki)