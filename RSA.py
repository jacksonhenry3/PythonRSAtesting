#simply to automate some stuff.
def exploop(array,power):
	newarray = []
	for i in array:
		newarray.append(int(i**power%N))
	return(newarray)

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
Message = [3,1,4,2,5,6,7,9,0,76,5,4,3,5,8]

EncryptedMessage = exploop(Message,e)

#############
#MESSAGE DECRYPTION
DecryptedMessage = exploop(EncryptedMessage,d)
print(DecryptedMessage)