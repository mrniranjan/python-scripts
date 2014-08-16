# We are importing random module/feature
import random

# we are declaring a variable called guessesTaken which stores value 0
guessesTaken = 0

# print a string "Hello! what's your name?"
print ('Hello! What is your name?')
# take the user input and store the value in myName
myName = raw_input()

# create a variable number, which would store the return value
# from the function random.radint()
# random.radint(1, 20) , means it takes 2 arguments 1, 20 and returns a result 
# which is stored in number.
number = random.randint(1, 20)
# we are printing a string on console
print ('Well, ' + myName + ', I am thinking of a number between 1 and 20.')


# this is a while loop, here we are 
while guessesTaken < 6:
	print ('Take a guess')
	guess = input()
	guess = int(guess)
	
	guessesTaken += 1

	if guess < number:
		print ('Your guess is too low.')

	if guess > number:
		print ('Your guess is too high.')
	
	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print ('Good Job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses! ')

if guess != number:
	number = str(number)
	print ('Nope . The number I was thinking of was ' + number)
