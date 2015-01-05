import string
lowercase = string.ascii_lowercase
key =13
def encrypt(plain):
  cipher = ""
  for i in plain:
    cipher = cipher + lowercase[(lowercase.index(i)+key)%len(lowercase)]
  return cipher
def decrypt(cipher):
  plain = ""
  for i in cipher:
    plain = plain + lowercase[(lowercase.index(i)-key)%len(lowercase)]
  return plain

plain = 'asdf'
print encrypt(plain)
print decrypt(encrypt(plain))
