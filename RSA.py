############
#KEY GENERATION
def Phi(P,Q):
	"""where N = P*Q"""
	return((P-1)*(Q-1))

#these are two random prime numbers
P = 53
Q = 59
PhiN = Phi(P,Q)

# this is the PUBLIC key
#################
N = P*Q
#any small value that DOES NOT share a factor with Phi(n)
e = 3
################

#this is a PRIVATE value (the backdoor exponent)
k=2
d = (k*PhiN+1)/e%N

#d< (p-1)(q-1) s.t. de==1 mod (p-1)(q-1).


############
#MESSAGE ENCRYPTION
Message = 3120
EncryptedMessage = Message**e%N

#############
#MESSAGE DECRYPTION
print(EncryptedMessage**d%N)