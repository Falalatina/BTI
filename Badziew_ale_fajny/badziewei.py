

from Crypto.Cipher import AES
from base64 import b64decode
key ='YELLOW SUBMARINE'
iv = "\x00" * 16
iv = iv.replace('%',r'\x')

#XOR-ing function
def xor_strings(a, b):
    return "".join(chr(ord(a1) ^ ord(b1)) for a1, b1 in zip(a, b))

#Taking input file and converting it into a single string 
file = open('10.txt','r')
data = file.read()
data = b64decode(data)
block = 16

obj = AES.new(key, AES.MODE_ECB)

def split_len(string, size):
    return [string[i:i+size] for i in range(0, len(string), size)]

mylist = split_len(data,block)


decrypted = ""
for i in range (0,len(mylist)):
     mystr = obj.decrypt(mylist[i])
     if (i==0):
          decrypted = decrypted + xor_strings(mystr,iv)
     else:
          decrypted = decrypted + xor_strings(mystr, mylist[i-1])
print(decrypted)