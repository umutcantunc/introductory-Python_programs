sinir = int(input("Hangi sayıya kadar 3'ün katları hesaplansın?\n(Girilen sayı dahil değil):"))
for i in range(1,sinir):
    if i % 3 != 0:
        continue
    print(i)