# applyCipher.py
# A program encrypt/decrypt user text
# using Caesars Cipher 
#
# Author: rc.moralesmarin.karla [at] leadps.org

# Makes a mapping of encoded alphabet to decoded alphabet 
# arguments: keys
# returns: dictionary of mapped lettersn
def createDictionary(key):

	#placeholder
	return {}

# asks the user for the encoded/decoded message
# arguments: none
# return: encoded message 
def getMessage():
	pass

# for each letter in the message, decodes and records 
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	pass

# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(message):
	pass 


# execution starts here

# ask user for key
print("What key would you like to use to decode?")
key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)

printMessage(decodedMessage)
