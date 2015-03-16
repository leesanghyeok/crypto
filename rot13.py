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
