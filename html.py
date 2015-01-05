import string
oldtab = ['&','<','>','\'','"']
newtab = ['&amp;','&lt;','&gt;','&#39;','&quot;']

def encode(plain):
  chiper = plain 
  for i in  range(len(oldtab)):
    chiper = string.replace(chiper,oldtab[i],newtab[i])
  return chiper

def decode(chiper):
  plain = chiper
  for i in range(len(oldtab)):
    plain = string.replace(plain,newtab[i],oldtab[i])
  return plain

print encode('< > \' \" &')
print decode(encode('< > \' \" &'))
