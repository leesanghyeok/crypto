import string
tab = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
def splitCount(s, count):
  return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]
def encode(plain):
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

def decode(cipher):
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
      plain = plain + ord(int(i,2))
  return plain 

