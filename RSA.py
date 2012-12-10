Message = "hello"

from ChunkedRSA import *

[P,Q,e] = [53,59,3]
N = P*Q

publicKey = [N,e]

privateKey = GeneratePrivateKey(P,Q,e)

NumericalMessage = Numerify(Message)

encryptedMessage = encrypt(NumericalMessage,e,P*Q)
M = decrypt(encryptedMessage,privateKey,N)
print(Denumerificate(M))