print(""" ************************************
Calculator Program
"+" "-" "*" "/"    just use these
**********************************
""")
a = int(input("First number:"))
b = int(input("Second number:"))
process =input("Process:")
if process == "+":
    print("{} + {} = {}".format(a,b,a+b))
elif process == "-":
    print("{} - {} = {}".format(a,b,a-b))
elif process == "*":
    print("{} * {} = {}".format(a,b,a*b))
if process == "/" and b !=0:
    print("{} / {} = {}".format(a,b,a/b))
elif b == 0:
    print("division-by-zero error")
else:
    print("ERROR")
