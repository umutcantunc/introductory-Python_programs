piramit_yukseklik = int(input("Piramitin yüksekliğini belirtin: "))

bosluk_uzunlugu = piramit_yukseklik #degisken adı karmasıklıgı olmamısı ıcın ıkı degısken adı kullanıldı.
yildiz_uzunlugu = 1

for i in range(1,piramit_yukseklik+1):

    for j in range(bosluk_uzunlugu,0,-1):
        print((" " * j) + ("*" * yildiz_uzunlugu))
        yildiz_uzunlugu +=2
        bosluk_uzunlugu -=1
