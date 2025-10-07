print("""
**************************************************************************
İki sayı girerek üçgenin dik kenarlarının alabileceği aralığı belirleyin
**************************************************************************
""")

s1, s2 = int(input("1.aralığı giriniz:")), int(input("2.aralığı giriniz:"))

def pisagor():
    liste = []
    for i in range(s1,s2+1):
        for j in range (s1,s2+1):
            c = (i ** 2 + j ** 2) ** (1/2)
            if c == int(c):
                if i > j:
                    continue
                liste.append((i,j,int(c)))
    return liste

sayac = 0
for i in pisagor():
    sayac += 1
    print("{}.üçgen -->".format(sayac),i)
