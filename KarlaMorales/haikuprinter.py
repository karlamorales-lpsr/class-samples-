print("Hi, welcome to the haiku reader")
print('choose...')
print('(3)For a haiku about a silly person.')
print('(4)For a haiku about writing haikus.')

choice = int(raw_input())
thirdhaiku = open('haiku3.txt','r')
forthhaiku = open('haiku4.txt','r')
if choice == 3: 
	print(thirdhaiku.read())
else:
	print(forthhaiku.read()) 
	
