
import sys, math
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890/*()_-,<>+=%$#@& ~{}[]\|!?.:;"'

content1=[0,0,0]
content2=[0,0,0]
# def main():

# 	filename = 'encrypted_file.txt' # The file to write to/read from.
# 	mode = int(input("choose mode 1 for encrypt 0 for decrypt: ")) # Set to either 'encrypt' or 'decrypt'.
# 	if mode == 1:
# 		message=input("Enter Your message: ")
# 		encryptedText = encryptAndWriteToFile(message)
# 		print('Encrypted text:')
# 		print(encryptedText)

# 	elif mode == 0:
# 		message2=input("Enter The Encrypted Text: ")
# 		decryptedText = readFromFileAndDecrypt(message2)
# 		print('Decrypted text:')
# 		print(decryptedText)

def getBlocksFromText(message, blockSize):
	for character in message:
		if character not in SYMBOLS:
			print('ERROR: The symbol set does not have the character %s' %(character))
			print(character)
			sys.exit()
	blockInts = []
	for blockStart in range(0, len(message), blockSize):
		blockInt = 0
		for i in range(blockStart, min(blockStart + blockSize,len(message))):
			blockInt += (SYMBOLS.index(message[i])) * (len(SYMBOLS) **(i % blockSize))
		blockInts.append(blockInt)
	return blockInts
def getTextFromBlocks(blockInts, messageLength, blockSize):
	message = []
	for blockInt in blockInts:
		blockMessage = []
		for i in range(blockSize - 1, -1, -1):
			if len(message) + i < messageLength:

				charIndex = blockInt // (len(SYMBOLS) ** i)
				blockInt = blockInt % (len(SYMBOLS) ** i)
				blockMessage.insert(0, SYMBOLS[charIndex])
		message.extend(blockMessage)
	return ''.join(message)
def encryptMessage(message, key, blockSize):
	encryptedBlocks = []
	n, e = key
	for block in getBlocksFromText(message, blockSize):
 		encryptedBlocks.append(pow(block, e, n))
	return encryptedBlocks

def decryptMessage(encryptedBlocks, messageLength, key, blockSize):
	decryptedBlocks = []
	n, d = key
	for block in encryptedBlocks:
		decryptedBlocks.append(pow(block, d, n))
	return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)

# def readpriKeyFile(content1):
# 	content1=list(map(int,input("Enter the private key: ").strip().split(',')))
# 	content1=[0,0,0]
# 	keySize, n, EorD = content1[0],content1[1],content1[2]
# 	return (int(keySize), int(n), int(EorD))

# def readpubKeyFile(content2):
# 	content2=list(map(int,input("Enter the public key: ").strip().split(',')))
# 	keySize, n, EorD = content2[0],content2[1],content2[2]
# 	return (int(keySize), int(n), int(EorD))

# def encryptAndWriteToFile(message,blockSize=None):
# 	keySize, n, e = readpubKeyFile(content2)
# 	if blockSize == None:
# 		blockSize = int(math.log(2 ** keySize, len(SYMBOLS)))
# 	if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
# 		sys.exit('ERROR: Block size is too large for the key and symbolset size. Did you specify the correct key file and encryptedfile?')
# 	encryptedBlocks = encryptMessage(message, (n, e), blockSize)
# 	for i in range(len(encryptedBlocks)):
# 		encryptedBlocks[i] = str(encryptedBlocks[i])
# 	encryptedContent = ','.join(encryptedBlocks)
# 	encryptedContent = '%s_%s_%s' % (len(message), blockSize,encryptedContent)
# 	return encryptedContent

# def readFromFileAndDecrypt(message2):
# 	keySize, n, d = readpriKeyFile(content1)
# 	messageLength, blockSize, encryptedMessage = message2.split('_')
# 	messageLength = int(messageLength)
# 	blockSize = int(blockSize)
# 	if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
# 		sys.exit('ERROR: Block size is too large for the key and symbolset size. Did you specify the correct key file and encryptedfile?')
# 	encryptedBlocks = []
# 	for block in encryptedMessage.split(','):
# 		encryptedBlocks.append(int(block))
# 	return decryptMessage(encryptedBlocks, messageLength, (n, d),blockSize)

	
# main()