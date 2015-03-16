import string
lower = string.ascii_lowercase

def equalstr(st,length):
  newstr = ""
  j =0
  for i in range(length):
    newstr = newstr + st[j]
    j=j+1
    if j == len(st):
      j = 0
  return newstr

def vigenen(plain,key):
  nkey = equalstr(key,len(plain))
  cipher = ""
  for i in range(len(plain)):
    cipher = cipher + lower[(lower.index(plain[i])+lower.index(nkey[i]))%len(lower)]
  return cipher

def vigende(cipher,key):
  nkey = equalstr(key,len(cipher))
  plain = ""
  for i in range(len(cipher)):
    plain = plain + lower[(lower.index(cipher[i])-lower.index(nkey[i]))%len(lower)]
  return plain 

if __name__=='__main__':
  plain = "helloworld"
  key = "clang"
  print vigenen(plain,key)
  print vigende(vigenen(plain,key),key)
