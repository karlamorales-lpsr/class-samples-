import random

n = random.randint(1,1000)

print("Choose a number between 1-1000")

userguess = int(raw_input())

while userguess != n:
	
	if userguess < n:
        	print(" na too low. ")
		userguess = int(raw_input())
	if userguess > n:
	        print(" na too high. ")
		userguess = int(raw_input())
if userguess == n:
	print("oh yup thats it")
