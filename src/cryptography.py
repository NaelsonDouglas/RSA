import random

def gcd(a,b):
	"""Compute the greatest common divisor of a and b"""
	while b > 0:
		a, b = b, a % b
	return a

def coprime(a, b):
	return gcd(a, b) == 1
	
def lcm(a, b):
	"""Compute the lowest common multiple of a and b"""
	return a * b / gcd(a, b)


def find_congruent(totient,e):
	for d in range(1,totient):
		if d*e % totient ==1:
			return d


def is_prime(num, test_count):
	if num == 1:
		return False
	if test_count >= num:
		test_count = num - 1
	for x in range(test_count):
		val = random.randint(1, num - 1)
		if pow(val, num-1, num) != 1:
			return False
	return True


def gen_prime(n):
	while True:
		p = random.randint(2**(n-1), 2**n)
		if is_prime(p, 1000):
			return p


def decrypt(private_key,message):
	cyphred=""
	for c in message:
		chr_utf = ord(c)
		encrypt_chr_utf = chr_utf^(private_key[1]) % private_key[0]-4
		

		cyphred = cyphred+chr(encrypt_chr_utf)
	return cyphred


def setup(private_key=-1,public_key=-1):
	if private_key == -1 or public_key == -1:
		p = gen_prime(5)
		q = gen_prime(5)
		n = p*q
		tot = (p-1)*(q-1)
		e = random.randint(1,tot)

		d = find_congruent(tot,e)
		if d == None:
			return setup(private_key,public_key)
		pub_k = (n,e)
		priv_k = (n,d)
		if False:
			print("p:"+str(p))
			print("q:"+str(q))
			print("n:"+str(n))
			print("tot:"+str(tot))
			print("e:"+str(e))
			print("d:"+str(d))

		return (pub_k,priv_k)


def decrypt(priv_key,message):
	uncyphred_msg=""
	for char in message:
		c = ord(char)
		uncyphred_char = pow(c,(priv_key[1])) % priv_key[0]
		uncyphred_msg = uncyphred_msg+chr(uncyphred_char)
	return uncyphred_msg

def encrypt(pub_key,message):
	cyphred_msg=""
	for char in message:
		c = ord(char)
		cyphred_char = pow(c,(pub_key[1])) % pub_key[0]		
		cyphred_msg = cyphred_msg+chr(cyphred_char)
	return cyphred_msg

if False:
	keys = setup()
	print(keys)
	print("\n")
	m = "Lorem ipsum"
	print("Mensagem: "+m)
	m = encrypt(keys[0],m)
	print("Mensagem criptografada: "+m)
	m = server.decrypt(keys[1],m)
	print("Mensagem revertida: "+m)
	print("\n")