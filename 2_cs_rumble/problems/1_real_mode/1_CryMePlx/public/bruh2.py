import binascii
import pwn
#from operator import xor





encrypted_flag = binascii.unhexlify(b"287bade7eb9801a0e5257e5b4a57ab6a263a8b30fa576617")
text = b"sanjivsanjivsanjiv"
encrypted_text = binascii.unhexlify(b"3a78abe4ec8f04e1e62e79425157b720263f")


blob = pwn.xor(encrypted_text, encrypted_flag)
flag = pwn.xor(blob, text)

#blob = encrypted_text^encrypted_flag
#flag = blob^text
print(flag)