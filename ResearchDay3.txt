AES
●	AES (Advanced Encryption Standard) 128-bit symmetric encryption
●	There are 10 rounds for 128-bit keys, 12 rounds for 192-bit keys and 14 rounds for 256-bit keys.
●	Flowchart
○	https://www.researchgate.net/figure/AES-encryption-flowchart_fig3_227063109




●	SubBytes
○	Each byte is substituted by another byte. Its performed using a lookup table also called the S-box.
●	ShiftRows
○	This step is just as it sounds. Each row is shifted a particular number of times.
■	The first row is not shifted 
■	The second row is shifted once to the left. 
■	The third row is shifted twice to the left. 
■	The fourth row is shifted thrice to the left.
●	MixColumns
○	This step is basically a matrix multiplication. Each column is multiplied with a specific matrix and thus the position of each byte in the column is changed as a result.




Hash Function
●	Trapdoor Function
○	f(x) → y
○	f-1(y) ↛ x
●	Enc(m) = c



SHA
●	SHA-2 (Secure Hash Algorithm 2) is a set of cryptographic hash functions
●	The SHA-2 family consists of six hash functions with digests (hash values) that are 224, 256, 384 or 512 bits:



BCRYPT
●	Bcrypt is a cryptographic hash function designed for password hashing and safe storing in the backend of applications in a way that is less susceptible to dictionary-based cyberattacks.
●	The cost factor makes bcrypt a slow algorithm that takes significantly more time to produce a hash key, turning it into a safe password-storing tool.



PBKDF2
●	Password-Based Key Derivation Function 2 (PBKDF2) makes it harder for someone to guess your account password through a brute-force attack.



Blockchain
Go to my "Cagchain" repository for a blockchain with blocks where you can mine them