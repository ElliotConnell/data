#Write a guessing game where the user has to guess a secret number. 
#After every guess the program tells the user whether their number was too large or too small. 
#At the end the number of tries needed should be printed. 
#It counts only as one try if they input the same number multiple times consecutively.


#generate and store random number

import random



number = random.randint(0,100)


#ask the user to input a number

query = int(input("Please select a number between 0 and 100: "))
count = 0

while query != number:



#if the number is high 
	if query <= number:
		print("Higher")
		query = int(input("Please select another number: "))
		if query != query:
			count += 1
			




#if the number is low
	elif query >+ number:
		print("Lower")
		query = int(input("Please select another number: "))
		if query != query:
			count += 1
			


#if it is the correct number
else:
	count += 1
	print("Correct")

	




#count how many times the loop happens
print("Nice Work! You took " + str(count) + " guesses")

#keep track of number and only count if new number