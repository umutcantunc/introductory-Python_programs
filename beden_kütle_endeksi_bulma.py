print("Beden Kitle Endeksi Hesaplama Programı")
boy = int(input("Boyunuzu girin:"))
kilo = int(input("Kilonuzu girin:"))
beden_kitle_endeksi = kilo / (boy/100)**2
print("Beden Kitle Endeksiniz: {}".format(beden_kitle_endeksi))
