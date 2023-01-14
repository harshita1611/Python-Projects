import random
correct = random.randrange(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {correct}")

print("choose a level :easy or hard")
choice = input()
low =1 
high = 100
def binary_search (element):
	mid = (low+high)/2
	if element == mid :
		print(f"element {element} found ")
	elif  element<mid :
		print("You , loose Try a lower number")
	elif  element>mid :
		print("You , loose Try a greater number")
if choice=="easy" :
	attempts=10
	print("You get 10 attempts")
	for i in range(1,10) :
		print("Make a guess")
		guess = int(input())
		binary_search(guess)
		
if choice=="hard":
	attempts =5
	print("You get 5 attempts")


