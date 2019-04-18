def encrypt(pub_key,message):
	cyphred_msg=""
	for char in message:
		c = ord(char)
		cyphred_char = pow(c,(pub_key[1])) % pub_key[0]		
		cyphred_msg = cyphred_msg+chr(cyphred_char)
	return cyphred_msg