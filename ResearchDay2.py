Symmetrical Encryption
In symmetrical encryption, both parties share the same key to encrypt and decrypt. This can be visualized as follows:
Alice: c = Enck(m) 
Bob: m = Deck(c)



Diffie-Hellman (DH)
Diffie-Hellman is a method used to securely exchange cryptographic keys over a public channel. It is as follows:
Alice                                 Bob
skA                                   skB 
g, n (public values)
pkA = g^skA mod n       <---->       pkB = g^skB mod n
K = (pkB)^skA mod n                  K = (pkA)^skB mod n    
=(g^skB)^skA mod n                   =(g^skA)^skB mod n
=g^(skB*skA) mod n                   =g^(skA*skB) mod n



Asymmetrical Encryption
In asymmetrical encryption, a key-pair (public and private) is generated as follows:

k → (pk, sk)
pk → public key
sk → private key
Encryption and decryption operations are performed as follows:

Encpk(m) = c
Decpk(c) = m
Some examples of this type of encryption include ElGamal and RSA.



Co-Prime Numbers
The greatest common denominator (GCD) of 'a' and 'b' is the largest integer that evenly divides both 'a' and 'b'.

For example, gcd(16, 24) = 8.

Two numbers, 'a' and 'b', are coprime if gcd(a, b) = 1.

Practice:
gcd(264, 122) = 264/122 = xk + n
264 = 122 x 2 + 20

gcd(122, 20) = 122/20 
122 = 20 x 6 + 2

gcd(20, 2) = 20/2 
20 = 2 x 10 + 0

gcd(2, 0) = 2



Modular Arithmetic
'a mod n' gives the remainder of a/n.

For example, 87 mod 16:
87/16 = 5.4375
5.4375 - 5 = 0.4375
0.4375 x 16 = 7
So, 87 mod 16 = 7



RSA (Rivest–Shamir–Adleman)
In RSA, encryption and decryption operations are performed as follows:

Encpk(m) = m^e mod n
Decsk(c) = c^d mod n
Where:

pk = (n, e)
sk = (n, d)
The values of 'n', 'e', and 'd' are chosen as follows:

Choosing 'n'
'n' is the product of two large prime numbers, 'p' and 'q', i.e., n = pq.

Choosing 'e'
'e' is chosen such that 1 < e < Ф(n) and e is co-prime to Ф(n). Here, the encryption operation is m^e mod n.

Choosing 'd'
'd' is calculated using the formula: d = (1 + kФ(n))/e.

For a more practical understanding, consider the following example:

Practice
1) Pick p, q → both prime numbers
p = 11, q = 13

2) Calculate n and Ф(n) 
n = p*q = 11*13 = 143
Ф(n) = (p - 1)*(q - 1) = 10*12 = 120

3) Pick e such that 1 < e < Ф(n) and gcd(e, Ф(n)) = 1
e = 107

4) Calculate d 
d = (1 + kФ(n))/e = 107^-1 mod 120 = 83

So, we have:
n = 143, Ф(n) = 120, pk = e = 107, sk = d = 83, m = 125

Now, perform encryption and decryption:

Enc107(125) = 125^107 mod 143 = 5 (c)

Receiver:
c = 5
Dec83(c) = c^83 mod n = 5^83 mod 143 = 125 (m)



Authentication
The current communication scheme does not avoid man-in-the-middle attacks, so we can't be sure if messages in transit have not been tampered with or if the people we are talking to are who we think they are.

Message authentication codes (MAC) can help with this problem:
Sigk(m) = tag
Verktag

There are symmetric and asymmetric encryption algorithms, including the Digital Signature Standard (DSS).



DSS (Digital Signature Standard)
In DSS:
sk = x, 0 < x < q
pk = g^x mod p



Signing
To sign a message:
1) Choose k, 0 < k < q using a Pseudo-Random-Number Generator (PRNG)
2) Calculate r = (g^k mod p) mod q
3) Solve for s in the equation h(m) = xr + ks mod q (where x is your secret key). This is known



