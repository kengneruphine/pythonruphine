#program to play the game of guess the number
import random

def guessGame():
	number = random.randrange(1,1001)
	print ''' 
		I have a number between 1 and 1000
         can you guess the number?
         please type your first guess
      '''
	return number  


number = guessGame() 
guess = int(raw_input("Enter your guess:"))

while 1:
	if number == guess :
		print "Excellent ,you gussed the number"
		print "Would you like to play agin (y or n)"
		ans = raw_input("->")
		if ans == 'y':
			number = guessGame()
			guess = int(raw_input("Enter your guess:"))

		else:
			break

	else:
		if guess > number:
			print "Too high,Try again"
			guess = int(raw_input("Enter your guess:"))

		else:
			print "Too low,Try again"
			guess = int(raw_input("Enter your guess:"))



