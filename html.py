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
