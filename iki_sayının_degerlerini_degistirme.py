print("Hokus Pokus... Sayılar Yer Değişecek :)")
a = int(input("Birinci sayıyı giriniz:"))
b = int(input("İkinci sayıyı giriniz:"))
print("Birinci Sayınız",a)
print("İkinci Sayınız",b)
print("Ama şimdi değiştiriyoruz...")
a,b=b,a
print("Artık birinci sayınız:",a)
print("Artık ikinci sayınız:",b)