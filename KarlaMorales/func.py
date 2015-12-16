# sets doubleIt as a functin that multiplies the input by 2 

def doubleIt(myNum):
# sets a result that will hold the answer to myNum * 2 
  myResult = myNum * 2
#
  return myResult
 
print(doubleIt(3))
print(doubleIt(5))
 
print("Enter a number.")
num = int(raw_input())
print("Ok, here you go: " + str(doubleIt(num)))


