from Crypto.Cipher import AES
from Crypto.Util.number import *
from os import urandom

key = urandom(16)
iv = urandom(16)

def pad(s):
	s += (16 - (len(s) % 16))*(chr(16 - (len(s) % 16)))
	return s

def encryption(pt):
	x = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode('base64')
	pt = pt + x
	pt = pad(pt)
	assert len(pt) % 16 == 0
	obj1 = AES.new(key, AES.MODE_ECB)
	c = obj1.encrypt(pt)
	return c


s = ""
for z in range(20):
	for i in range(1, 17):
		input_str = 'a'*(16-i)
		ct = encryption(input_str)[16*z:16*z+16]
		for j in range(256):
			ct1 = encryption(input_str + s + chr(j))[16*z:16*z+16]
			if ct == ct1:
				s += chr(j)
				break
print s
