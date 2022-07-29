import login
import new_user
print("Papers")
print("Welcome User")
print("Press 1 to navigate to Login Page")
print("Press 2 to navigate to Signup Page")
inp = int(input())
a = []
if inp == 1:
    login.Login()
elif inp == 2:
    new_user.newuser()
        
