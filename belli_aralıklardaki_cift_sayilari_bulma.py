print("Sayılarınızı giriniz:")
aralik1,aralik2 = int(input()), int(input())
liste = [i for i in range(aralik1,aralik2 + 1) if i % 2 == 0]
print("{} ile {} arasındaki çift sayılar:".format(aralik1,aralik2),liste)

liste = [i for i in range(aralik1,aralik2 + 1) if i % 2 != 0]
print("{} ile {} arasındaki tek sayılar:".format(aralik1,aralik2),liste)