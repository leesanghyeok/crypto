import string
import random
lowercase = string.ascii_lowercase
base64tab = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
htmloldtab = ['&','<','>','\'','"']
htmlnewtab = ['&amp;','&lt;','&gt;','&#39;','&quot;']


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

def hexen(plain):
  cipher = ""
  for i in plain:
    cipher = chiper + hex(ord(i))[2:]
  return cipher

def hexde(cipher):
  plain = ""
  mc = splitCount(cipher,2)
  for i in mc:
    plain = plain + chr(int(i,16))
  return plain

def htmlen(plain):
  cipher = plain 
  for i in  range(len(htmloldtab)):
    cipher = string.replace(chiper,htmloldtab[i],htmlnewtab[i])
  return cipher

def htmlde(cipher):
  plain = cipher
  for i in range(len(htmloldtab)):
    plain = string.replace(plain,htmlnewtab[i],htmloldtab[i])
  return plain

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












