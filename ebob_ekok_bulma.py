def ebob(s1,s2):
    s1bolen = []
    s2bolen = []
    for i in range(2,s1+1):
        for j in range(2,s2+1):
            if s1 % i == 0 and s2 % i == 0:
                s1bolen.append(i)
            if s1 % j == 0 and s2 % j == 0:
                s2bolen.append(j)
    for i in s1bolen[::-1]:
        for j in s2bolen[::-1]:
            if i == j:
                return i
    return 1


while True:
    s1 = input("1.sayıyı giriniz:")

    if s1 == "q":
        print("Program sonlandı.")
        break
    if int(s1) <=1:
        print("Sadece 1'den büyük pozitif tam sayı giriniz.")
        continue

    s2 = input("2.sayıyı giriniz:")

    if s2 == "q":
        print("Program sonlandı.")
        break
    if int(s2) <=1:
        print("Sadece 1'den büyük pozitif tam sayı giriniz.")
        continue

    else:
        s1,s2 = int(s1),int(s2)
        print("{} ile {} --> EBOBU:".format(s1,s2),ebob(s1,s2))
        print("{} ile {} --> EKOKU:".format(s1,s2),(s1 * s2)//ebob(s1,s2))