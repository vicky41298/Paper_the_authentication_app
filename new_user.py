from ast import Pass
import login
import password_validation
import email_validation
def newuser():
    print("Welcome new User!!... Hope you enjoy Papers!")
    name = input("Enter your name:")
    email = input("Enter your email:")
    passw = input("Enter your Password:")
    Password1 = input("Re-enter your Password:")
    mailv = email_validation.mailvalid(email)
    passv = password_validation.passw(passw)
    if mailv == True and passv == True and passw == Password1:
        a = [name,email,passw]
        f = open("signup.txt","a")
        f.write(' '.join(a))
        f.write('\n')
        f.close()
        print("Successfully registered!")
        login.Login()
    else:
        newuser()