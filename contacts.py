print("Welcome To Contacts!")
print("What would you like to do?")
print("(1) Add a phone number.")
print("(2) Print the full list of contacts.")
print("(3) Enter a name to retrieve that contact's phone number.")
print("(0) Exit the Contacts App.")

option = int(raw_input())

if option == "1":
	print("What's the name of your contact?")
	contactName = str(raw_input())
	print("What's the phone number of your contact?")
	contactContact = int(raw_input())
 	contact[name] = number
 	print("New Contact Saved")

 	if option == 2:
 		print(" ")
 		print("find Contact")
 		print(" ")
 		print("Contact Name:")
 		print(" ")
 		name = raw_input()
 		print(" ")
 		print("Here's you go")
 		print(" ")
 		print(contact[name])
 
 	if option == 3:
 		print(" ")
                 print("Contacts")
 		print(" ")
            	 print(contact)
