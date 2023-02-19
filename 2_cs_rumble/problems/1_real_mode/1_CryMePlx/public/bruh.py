import binascii
import pwn
#from operator import xor





encrypted_flag = binascii.unhexlify(b"a3cf97f7ac889455e910f0baa29a2e53b009ed8bc144addc78")
text = b"qwertyuiopqwertyuiopqwertyuiop"
encrypted_text = binascii.unhexlify(b"91eba0fe96c18f5fe313deacb58d054cb00ee48ede55bdc071a1d90202ce")


blob = pwn.xor(encrypted_text, encrypted_flag)
flag = pwn.xor(blob, text)

#blob = encrypted_text^encrypted_flag
#flag = blob^text
print(flag)