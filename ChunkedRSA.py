#simply to automate some stuff.
def exploop(array,power,N):
	newarray = []
	for i in array:
		newarray.append(int(i**power%N))
	return(newarray)

#generates private key
def GeneratePrivateKey(P,Q,e):
	N = P*Q
	PhiN = (P-1)*(Q-1)
	k = 2 #where does this k come from???
	d = (k*PhiN+1)/e%N
	return(d)

#encrypts a message
def encrypt(Message,e,N):
	encryptedMessage = exploop(Message,e,N)
	return(encryptedMessage)

#decrypt a message
def decrypt(encryptedMessage,d,N):
	 Message = exploop(encryptedMessage,d,N)
	 return(Message)

def Numerify(message):
	array = ["""1""",""" ""","""2""","""3""","""4""","""5""","""6""","""7""","""8""","""9""","""0""","""q""","""w""","""e""","""r""","""t""","""y""","""u""","""i""","""o""","""p""","""a""","""s""","""d""","""f""","""g""","""h""","""j""","""k""","""l""","""z""","""x""","""c""","""v""","""b""","""n""","""m""","""Q""","""W""","""E""","""R""","""T""","""Y""","""U""","""I""","""O""","""P""","""A""","""S""","""D""","""F""","""G""","""H""","""J""","""K""","""L""","""Z""","""X""","""C""","""V""","""B""","""N""","""M""","""~""","""!""","""@""","""#""","""$""","""%""","""^""","""&""","""*""","""_""","""+""","""-""","""=""","""[""","""]""","""\\""","""{""","""}""","""|""",""":""",""" " """,""":""","""'""","""<""",""">""","""?""",""",""",""".""","""/"""]
	dictionary = {}
	for j in range(len(array)):
		dictionary[array[j]] = j

	NumericMessage = []
	for i in message:
		NumericMessage.append(dictionary[i])

	return(NumericMessage)

def Denumerificate(NumericMessage):
	array = ["""1""",""" ""","""2""","""3""","""4""","""5""","""6""","""7""","""8""","""9""","""0""","""q""","""w""","""e""","""r""","""t""","""y""","""u""","""i""","""o""","""p""","""a""","""s""","""d""","""f""","""g""","""h""","""j""","""k""","""l""","""z""","""x""","""c""","""v""","""b""","""n""","""m""","""Q""","""W""","""E""","""R""","""T""","""Y""","""U""","""I""","""O""","""P""","""A""","""S""","""D""","""F""","""G""","""H""","""J""","""K""","""L""","""Z""","""X""","""C""","""V""","""B""","""N""","""M""","""~""","""!""","""@""","""#""","""$""","""%""","""^""","""&""","""*""","""_""","""+""","""-""","""=""","""[""","""]""","""\\""","""{""","""}""","""|""",""":""",""" " """,""":""","""'""","""<""",""">""","""?""",""",""",""".""","""/"""]
	dictionary = {}
	for j in range(len(array)):
		dictionary[j] = array[j]

	Message = ''
	for i in NumericMessage:
		Message+=str(dictionary[i])

	return(Message)
