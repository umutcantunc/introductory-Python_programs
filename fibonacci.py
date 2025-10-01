print("""
************************************
-Negative numbers show in reverse
-Press "0" to exit
************************************
""")
while True:
    number = int(input("Up to how many numbers do you want to see?:"))
    if number == 1 or number == -1:
        a,b= 1,1
        fibonacci = [a, b]
        print(fibonacci[0:1])
        continue
    if number == 2 or number == -2:
        a,b= 1,1
        fibonacci = [a, b]
        print(fibonacci)
        continue
    if number < 0:
        a,b= 1,1
        fibonacci = [a, b]
        for i in range(abs(number)-2):
            a,b = b,a+b
            fibonacci.append(b)
        print(fibonacci[::-1])
    if number > 0:
        a,b= 1,1
        fibonacci = [a, b]
        for i in range(number-2):
            a,b = b,a+b
            fibonacci.append(b)
        print(fibonacci)
    if number == 0:
        print("Exited")
        break