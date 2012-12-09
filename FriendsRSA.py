############
#KEY GENERATION
def Exp(P,Q):
    """where N = P*Q"""
    return((P-1)*(Q-1))

#these are two random prime numbers
P = 53
Q = 59
ExpN = Exp(P,Q)

# this is the PUBLIC key
#################
N = P*Q
#any small value that DOES NOT share a factor with Exp(N); this is your private key
d = 3
################
#d< (p-1)(q-1) s.t. de==1 mod (p-1)(q-1).
#this is your public key, which you tell everyone so they can send you messages.
e = (1/d)%ExpN


############
#MESSAGE ENCRYPTION
Message = 3128

EncryptedMessage = (Message**e)%N

#############
#MESSAGE DECRYPTION
print((EncryptedMessage**d)%N)
print((EncryptedMessage**d))