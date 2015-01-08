import string
import random

lowercase = string.ascii_lowercase
def _keygen():
  key = list(lowercase)
  random.shuffle(key)
  return key 

def encrypt(plain,key):
  cipher = plain
  tm = string.maketrans(lowercase,''.join(key))
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
  

def decrypt(cipher,key):
  plain = cipher
  tm = string.maketrans(''.join(key),lowercase)
  return cipher.translate(tm)
  

f1 = open("read.txt", 'r')
plain = f1.read()
f1.close()
#f2 = open('cipher.txt','w')
key = _keygen()
cipher = encrypt(plain,key)
print cipher
#f2.write(cipher)
#f2.close()
#f3 = open('cipher.txt','r')
#cipher = f3.read()
#f.3close
print decrypt(cipher,key)
