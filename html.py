import string
oldtab = ['&','<','>','\'','"']
newtab = ['&amp;','&lt;','&gt;','&#39;','&quot;']

def encode(plain):
  cipher = plain 
  for i in  range(len(oldtab)):
    cipher = string.replace(chiper,oldtab[i],newtab[i])
  return cipher

def decode(cipher):
  plain = cipher
  for i in range(len(oldtab)):
    plain = string.replace(plain,newtab[i],oldtab[i])
  return plain

print encode('< > \' \" &')
print decode(encode('< > \' \" &'))
