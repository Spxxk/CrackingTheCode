# Used AI to write like 25% of the stuff because I am bad at explaining

# Types of Ciphers
# ●	CAESAR CIPHER
# ●	Vernam Cipher

# Types of Attacks
# ●	Passive attacks
# ○	Involves an attacker passively monitoring or collecting data without altering or destroying it
# ●	Active attacks
# ○	An attacker attempts to alter, destroy, or disrupt the normal operation
# ●	The man-in-the-middle attack

# Games
# ●	Chosen-plaintext attack (CPA)
# ●	Chosen-ciphertext attack (CCA)

# Web requests
# ●	Allows your computer to send/receive information
# ●	A web server handles your requests and delivers the appropriate data
# ●	Two main types of requests
# ○	GET request
# ■	Ask for data
# ○	POST request
# ■	Send data
# ●	Inside a request
# ○	Destination
# ■	URL
# ■	Query parameters
# ●	What information you are requesting (?q = car)
# ○	Headers
# ■	How you are sending it
# ■	Describes the contents of the request
# ●	Content-Type
# ■	Describe the desired response
# ○	Body
# ■	The information you are trying to send

# Terminology
# ●	m → message
# ○	Thing we want to encrypt
# ●	k → key
# ○	Thing we use to encrypt
# ●	c → cipher text
# ○	Encrypted message
# ●	Enc → encryption function
# ●	Dec → decryption function
# ●	Enck(m) = c
# ●	Deck(c) = m
# ●	Enc = Dec (somtimes)

# Shannon’s Perfect Secrecy
# ●	Calude Elwood Shannon
# ●	 
# ●	One-time-pad
# ○	Enck(m) = m ⊕ k

# XOR
# ●	XOR gate (sometimes EOR, or EXOR and pronounced as Exclusive OR) is a digital logic gate that gives a true (1 or HIGH) output when the number of true inputs is odd. 
# ●	An XOR gate implements an exclusive or ( ) from mathematical logic; that is, a true output results if one, and only one, of the inputs to the gate is true.
# ●	OTP -> Enck (m) = m ⊕ this sign is basically xor k 

# ● The steps to encrypt and decrypt using the OTP are as follows:

# ● Encryption:
# ● You start with plaintext. For example, m1 = 10110101.
# ● Then you generate a random secret key of the same length. For example, k1 = 10010010.
# ● You combine the plaintext with the key using the XOR operation. The result is the ciphertext. For example, c1 = m1 ⊕ k1 = 00100111.
# ● Decryption:
# ● You start with the ciphertext. For example, c1 = 00100111.
# ● You have the same secret key used in the encryption. For example, k1 = 10010010.
# ● You combine the ciphertext with the key using the XOR operation. The result is the original plaintext. For example, m1 = c1 ⊕ k1 = 10110101.
# ● Note that for the OTP to be secure, each secret key must be truly random, at least as long as the plaintext, never reused in whole or part, and kept completely secret.

# ● In the context of the XOR operation you mentioned, the OTP refers to the XOR operation used to combine the plaintext and the key to produce the ciphertext, and to combine the ciphertext and the key to recover the plaintext.


# “Symmetric Encryption”
# ●	Enck(m) = c
# ●	Deck(c) = m
# ●	The key is the same in the decryption and encryption
# ○	Examples
# ■	Caesar cipher

# Asymmetric Encryption
# ●	k → (pk, sk)
# ●	pk → public key
# ●	sk → private key
# ●	Encpk(m) = c
# ●	Decpk(c) = m
# ○	When you encrypt, you use a public key.
# ○	When you decrypt, you use a private key.

# Key sharing
# ●	Meet and decide on a key
# ○	Generate new keys from our existing key
# ●	Devise a “handshake” method
# ●	Diffie-Hellman
# ○	g and n is public values
# ○ Each party chooses a private number. Let's denote these as a (Alice's private number) and b (Bob's private number)
# ○ They then calculate public values using g, n and their respective private number and exchange these public values. For example, Alice calculates A = g^a mod n and Bob calculates B = g^b mod n.
# ○ After the public values have been exchanged, each party can calculate the shared secret key by raising the received value to the power of their own private number and taking the modulus n. In mathematical terms, the shared secret (key) K is calculated by Alice as K = B^a mod n and by Bob as K = A^b mod n.

# ○ Remember, due to the properties of modular arithmetic, both Alice and Bob end up with the same value for K, despite going about it in slightly different ways. This shared secret can now be used as a key in symmetric cryptography.

# ○ For the Diffie-Hellman method to be secure, it is important that the private numbers a and b are kept secret. The values g, n, A, and B can be sent over an insecure network without compromising the security of the shared secret key.

# Symmetrical Encryption
# ●	Both share the same key to encrypt and decrypt 
#    Alice                    Bob
# ●	c = Enck(m) —> m = Deck(m)

# DH (Diffie-Hellman)
# Alice                                      Bob
# ●	skA                                      skB 
# ●	g, n (random public values)
# ●	pkA = gskA mod n                   pkB = gskB mod n
#                      —>           ←–
# ●	K = pkBskA mod n                   K = pkAskB mod n    
# ●	=(gskB)skA mod n                   =(gskA)skB mod n
# ●	=gskB skA mod n                    =gskA skB mod n

