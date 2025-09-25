print("""
*********************
SYSTEM LOGIN PROGRAM
*********************
""")
correct_username = "admin"
correct_password = "123"

username = input("Username:")
password = input("Password:")
if username == correct_username and password != correct_password:
    print("Wrong password")
elif username != correct_username and password == correct_password:
    print("Wrong username")
elif username != correct_username and password != correct_password:
    print("Wrong username and password")
else:
    print("Login successful")
