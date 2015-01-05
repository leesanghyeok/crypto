import string
import random

lower = string.ascii_lowercase
def keygen():
  key = list(lower)
  random.shuffle(key)
  return key 

def encrypt(plain):
  cipher = plain
  key = keygen()
  tm = string.maketrans(lower,''.join(key))
  return cipher.translate(tm)

def getNdic(text,N):
  sp = text.split(' ')
  splist = []
  for i in sp:
    if len(i) == N:
      if splist.count(i) == 0 :
        splist.append(i)
  dic = {}
  for i in splist:
    dic[i] = text.count(i)
  return getsortdic(dic)

def getsortdic(dic):
  dicval = dic.values()
  dicval.sort()
  return (dic,dicval)
  

def decrypt(cipher):
  cntdic = {} 
  for i in lower:
    cntdic[i] = cipher.count(i)
  key = "FMAPSGVRBNIlOToKHGsYLCUDWE"
  tm = string.maketrans(lower,key)
  cipher = cipher.translate(tm)
  print cipher
  print getsortdic(cntdic)
  dic3 = getNdic(cipher,3)
  print dic3
  dic1 = getNdic(cipher,2)
  print dic1
  
#  print cipher
  #return cipher  


#f = open("read.txt", 'r')
#plain = f.read()
#f.close()
#f = open('cipher.txt','w')
#f.write(encrypt(plain))
#f.close()
f = open('cipher.txt','r')
cipher = f.read()
f.close
print decrypt(cipher)
