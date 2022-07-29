from itertools import chain
import new_user
import password_validation
import login
def forgpass(username):
    file1 = open("signup.txt", "r").readlines()
    ind = 0
    ac = []
    for line in file1:
        c = line.split()
        ac.append(c)
    fl = list(chain.from_iterable(ac))
    for i in fl:
        c = fl.index(i)
        if i == username:
            ind = c + 1
        else:
            pass
    a = ''
    for i in range(len(fl)-1):
        if ind > 0:
            a = fl[ind]
    if len(a) > 0:
        print("Password available in DB")
        print("Kindly press 1 to reveal your password\nKindly Press 2 to reset your Password")
        inp = int(input())
        if inp == 1:
            print(a)
        elif inp == 2:
            passw = input("Enter your new Password: ")
            vi = password_validation.passw(passw)
            if vi == True:
                with open("signup.txt") as f:
                    newText=f.read().replace(a,passw)
                with open("signup.txt", "w") as f:
                    f.write(newText)
                print("Password Updated Successfully!")
            else:
                forgpass()
        login.Login()
    else:
        print("User not registerd, you are now being redirected to signup page....")
        new_user.newuser()

