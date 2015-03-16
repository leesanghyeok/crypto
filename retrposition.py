import string
import random

lowercase = string.ascii_lowercase
def _keygen():
  key = list(lowercase)
  random.shuffle(key)
  return key 

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
  
def trposen(plain,key):
  cipher = plain
  tm = string.maketrans(lowercase,''.join(key))

  return cipher.translate(tm)
def trposde(cipher,key):
  plain = cipher
  tm = string.maketrans(''.join(key),lowercase)
  return cipher.translate(tm)
  
if __name__=='__main__':
  f1 = open("txt/read.txt", 'r')
  plain = f1.read()
  f1.close()
  key = _keygen()
  cipher = trposen(plain,key)
  print cipher
  print trposde(cipher,key)
