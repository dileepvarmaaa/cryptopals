from Crypto.Cipher import AES
from os import urandom
import random

key = urandom(16)

def pad(s):
	s += (16 - (len(s) % 16))*(chr(16 - (len(s) % 16)))
	return s

def encrypt(pt,key):
	prefix="varmaaaa"
	x="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode('base64')
	
	c=AES.new(key,AES.MODE_ECB)
	ct=c.encrypt(pad(prefix+pt+x))
	return ct

if __name__=="__main__":

	for i in range(1,17):
		pt="a"*i
		ct=encrypt(pt,key)
		if(ct[:16]==encrypt("a"*16,key)[:16]):     
			prefix_len=16-i
		
			break	
       
	junk=""
	for k in range (20):
		q=16+prefix_len*(k-1)   
		for j in range (1,16-prefix_len+1):
 			s="a"*(q-j)
 			b=encrypt(s,key)[16*k:16*k+16]
			for i in range (256):
				ct=encrypt(s+junk+chr(i),key)[16*k:16*k+16]
				if(ct==b):		
					junk=junk+chr(i)
					break

		print(junk)

