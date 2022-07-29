import re
def passw(inp):
  if len(inp)<8 or len(inp)>32:
    print('Your password must be more than 8 charcter and less than 32 character.')
    return False
  elif not re.search('[a-z]',inp):
    print("Kindly include a LowerCase character in your password.")  
    return False
  elif not re.search('[A-Z]',inp):
    print("Kindly include a UpperCase character in your password.")
    return False 
  elif not re.search('[0-9]',inp):
    print("Kindly include a number in your password.")
    return False
  elif not  re.search('[@#$]',inp):
    print("Kindly include a special character (@,#,$) in your password.")
    return False
  else:
    return True
