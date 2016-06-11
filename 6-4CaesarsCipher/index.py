# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher

import string

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	lower = list(string.ascii_lowercase)
 	upper = list(string.ascii_uppercase)
 	alphabet = {}
 	count = 0
 	while count < 26:
 		alphabet[lower[(key + count) % 26]] = lower[1]
 		count = count + 1 
 	return alphabet


# gets the encrypted message from the user
# arguments: none
# returns: encoded message
def getMessage():
	print("what is your message?")
	message = raw_input()
	return message 

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	finalmsg = " " 
	for letter in message: 
		finalmsg = finalmsg + alphabet[1]
	return finalmsg

# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(message):
	print(message)


# execution starts here

# ask user for key
print("What key would you like to use to decode?")
key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)

printMessage(decodedMessage)

