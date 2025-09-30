print("""
**************************
Kullanıcı Giriş Programı
**************************
""")
system_username = "admin"
system_password = "1234"
kalan_hak = 3

while True:
    username = input("Username:")
    password = input("Password:")
    if username != system_username and password == system_password:
        print("Wrong username")
        kalan_hak -= 1
        print("Your remaining entry rights:", kalan_hak)
    elif username == system_username and password != system_password:
        print("Wrong password")
        kalan_hak -= 1
        print("Your remaining entry rights:", kalan_hak)
    elif username != system_username and password != system_password:
        print("Wrong username and password")
        kalan_hak -= 1
        print("Your remaining entry rights:", kalan_hak)
    else:
        print("Login Success")
        break
    if kalan_hak == 0:
        print("YOUR ENTRY RIGHTS ARE ENDED")
        break
