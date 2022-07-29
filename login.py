from itertools import chain
import email_validation
import new_user
import forgot_password
def Login():
    email = input("Enter your Email: ")
    Password = input("Enter your Password: ")
    #mailv = email_validation.mailvalid(email)
    file1 = open("signup.txt", "r").readlines()
    ind = 0
    ac = []
    for line in file1:
        c = line.split()
        ac.append(c)
    cl = list(chain.from_iterable(ac))
    for i in cl:
        c = cl.index(i)
        if i == email:
            ind = c + 1
    for i in range(len(cl)-1):
        if cl[ind] == Password:
            print(f"Login Successful.... Welcome {cl[ind-2]}")
            break
    else: 
        print("Username or Password is invalid...")
        print("If you are new to Pages press 1 to register yourself")
        print("If you forgot your password press 2 to retrive your old password")
        inpu = int(input())
        if inpu == 1:
            new_user.newuser()
        elif inpu == 2:
            email = input("enter your email: ")
            forgot_password.forgpass(email)