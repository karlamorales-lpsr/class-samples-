print("Welcome to Josephina's Quest!")
print("Enter the name of your character")

name = (raw_input())

print("Enter strength (1-10)")
strength = int(raw_input())

print("Enter health (1-10)")
health = int(raw_input())

print("Enter luck (1-10)")
luck = int(raw_input())

if health + luck + strength > 15:
	print("you gave your character too many points!")
else:
	print(name + " you have came to a fork in the road" + " " + "do you want to go right or left?")

leftOrRight = str(raw_input())
decision = leftOrRight 

if leftOrRight == decision:
	print("sorry you fell off a cliff :(")
else:
	print("you made it to the end of the rainbow!")

