n = int(input("Enter a number:"))
step = 0
while n != 1:
    if n % 2 == 0:
        step += 1
        n //= 2
        print("Step {} : {}".format(step,n))

    else:
        step += 1
        n = 3 * n + 1
        print("Step {} : {}".format(step,n))