def mailvalid(inp):
  li = list(inp)
  count = 0
  confirm = 0
  for i in li:
    if i == '@' or i == '.':
      count += 1
  if "@" not in li:
    print("Enter a valid email ID")
    return False
  else:
    if count == 2:
      a = li.index('@')
      b = li.index('.')
      if a < b:
        ac = li[:a]
        if len(ac) >= 4:
          confirm += 1
        lc = li[a+1:b]
        if len(lc) >= 3:
          confirm += 1
        vi = li[0]
        sym = ['!','@','#','$','%','^','&','*','(',')','/','-','+',';',':','[',']','{','}','.',',','`']
        if vi.isdigit() or vi in sym:
          confirm -= 1
        else:
          confirm += 1
    if confirm == 3:
      return True
    else:
      return False
