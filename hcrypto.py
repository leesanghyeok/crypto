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
import string
tab = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
def splitCount(s, count):
  return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]
def b64en(plain):
  plen = len(plain)
  mc = ""
  for ch in plain:
    mc = mc + bin(ord(ch))[2:].zfill(8)
  if plen%3!=0:
    mc = mc + (3-plen%3)*('0'*8)
  cc = splitCount(mc,6)
  cipher = ""
  for i in cc:
    if i=='0'*6:
      cipher = cipher + '='
    else:
      cipher = cipher + tab[int(i,2)]   
  return cipher 

def b64de(cipher):
  plain = "" 
  clen = len(cipher)
  mp = ""
  for i in cipher:
    if i=='=':
      mp = mp + '0'*6
    else:
      mp = mp + bin(tab.index(i))[2:].zfill(6)
  mc = splitCount(mp,8)

  for i in mc:
    if i!='0'*8:
      plain = plain + chr(int(i,2))
  return plain 

if __name__ == '__main__':
  plain = "asdf"
  print b64en(plain)
  print b64de(b64en(plain))
import string
lowercase = string.ascii_lowercase
key =13
def rot13en(plain):
  cipher = ""
  for i in plain:
    cipher = cipher + lowercase[(lowercase.index(i)+key)%len(lowercase)]
  return cipher
def rot13de(cipher):
  plain = ""
  for i in cipher:
    plain = plain + lowercase[(lowercase.index(i)-key)%len(lowercase)]
  return plain
if __name__=='__main__':
  plain = 'asdf'
  print rot13en(plain)
  print rot13de(rot13en(plain))
import string
oldtab = ['&','<','>','\'','"']
newtab = ['&amp;','&lt;','&gt;','&#39;','&quot;']

def htmlen(plain):
  cipher = plain 
  for i in  range(len(oldtab)):
    cipher = string.replace(cipher,oldtab[i],newtab[i])
  return cipher

def htmlde(cipher):
  plain = cipher
  for i in range(len(oldtab)):
    plain = string.replace(plain,newtab[i],oldtab[i])
  return plain
if __name__ == '__main__':
  print htmlen('< > \' \" &')
  print htmlde(htmlen('< > \' \" &'))
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
import string
def splitCount(s, count):
  return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]

def hexen(plain):
  cipher = ""
  for i in plain:
    cipher = cipher + hex(ord(i))[2:]
  return cipher

def hexde(cipher):
  plain = ""
  mc = splitCount(cipher,2)
  for i in mc:
    plain = plain + chr(int(i,16))
  return plain

if __name__ == "__main__":
  plain = 'asdf'
  print hexen(plain)
  print hexde(hexen(plain))
import string
lowercase = string.ascii_lowercase
def caesaren(plain,key):
  cipher = ""
  for i in plain:
    cipher = cipher + lowercase[(lowercase.index(i)+key)%len(lowercase)]
  return cipher
def caesarde(cipher,key):
  plain = ""
  for i in cipher:
    plain = plain + lowercase[(lowercase.index(i)-key)%len(lowercase)]
  return plain
if __name__ == '__main__':
  plain = 'asdf'
  key = 3
  print caesaren(plain,key)
  print caesarde(caesaren(plain,key),key)
