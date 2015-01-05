import string
lowercase = string.ascii_lowercase
def encrypt(plain,key):
  cipher = ""
  for i in plain:
    cipher = cipher + lowercase[(lowercase.index(i)+key)%len(lowercase)]
  return cipher
def decrypt(cipher,key):
  plain = ""
  for i in cipher:
    plain = plain + lowercase[(lowercase.index(i)-key)%len(lowercase)]
  return plain

plain = 'asdf'
key = 3
print encrypt(plain,key)
print decrypt(encrypt(plain,key),key)
