#Exercises on strings
#To check if a word doesnot have the letter 'e'
def has_no_e(word):
	for letter in word:
		if letter =='e':
			return False
	return True


print has_no_e('good')

#checks if letters of a word are in alphabetical order
def is_abecedarian(word):
	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_abecedarian(word[1:])

print is_abecedarian('dec')



