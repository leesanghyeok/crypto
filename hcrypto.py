import string
import random
lowercase = string.ascii_lowercase
base64tab = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
htmloldtab = ['&','<','>','\'','"']
htmlnewtab = ['&amp;','&lt;','&gt;','&#39;','&quot;']


def splitCount(s, count):
  return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]

def _keygen():
  key = list(lowercase)
  random.shuffle(key)
  return key 

def equalstr(st,length):
  newstr = ""
  j =0
  for i in range(length):
    newstr = newstr + st[j]
    j=j+1
    if j == len(st):
      j = 0
  return newstr

#base64
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
      cipher = cipher + base64tab[int(i,2)]   
  return cipher 

def b64de(cipher):
  plain = "" 
  clen = len(cipher)
  mp = ""
  for i in cipher:
    if i=='=':
      mp = mp + '0'*6
    else:
      mp = mp + bin(base64tab.index(i))[2:].zfill(6)
  mc = splitCount(mp,8)
  for i in mc:
    if i!='0'*8:
      plain = plain + ord(int(i,2))
  return plain 

#hex
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

#html
def htmlen(plain):
  cipher = plain 
  for i in  range(len(htmloldtab)):
    cipher = string.replace(cipher,htmloldtab[i],htmlnewtab[i])
  return cipher

def htmlde(cipher):
  plain = cipher
  for i in range(len(htmloldtab)):
    plain = string.replace(plain,htmlnewtab[i],htmloldtab[i])
  return plain

#caesar
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

#rot13
def rot13en(plain):
  cipher = ""
  for i in plain:
    cipher = cipher + lowercase[(lowercase.index(i)+13)%len(lowercase)]
  return cipher
def rot13de(cipher):
  plain = ""
  for i in cipher:
    plain = plain + lowercase[(lowercase.index(i)-13)%len(lowercase)]
  return plain

#transposition
def trposen(plain,key):
  cipher = plain
  tm = string.maketrans(lowercase,''.join(key))
  return cipher.translate(tm)

def trposde(cipher,key):
  plain = cipher
  tm = string.maketrans(''.join(key),lowercase)
  return cipher.translate(tm)

#vigenere
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







