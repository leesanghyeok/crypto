import string
lowercase = string.ascii_lowercase
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
if __name__ == '__main__':
  plain = 'asdf'
  key = 3
  print caesaren(plain,key)
  print caesarde(caesaren(plain,key),key)
