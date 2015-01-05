import string

def splitCount(s, count):
  return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]
def encode(plain):
  cipher = ""
  for i in plain:
    cipher = chiper + hex(ord(i))[2:]
  return cipher

def decode(cipher):
  plain = ""
  mc = splitCount(cipher,2)
  for i in mc:
    plain = plain + chr(int(i,16))
  return plain
print encode('abcd')
print decode(encode('abcd'))
