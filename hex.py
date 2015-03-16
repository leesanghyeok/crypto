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
