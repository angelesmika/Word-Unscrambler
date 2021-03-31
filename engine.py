# ACKNOWLEDGEMENTS
# Carlos Panganiban - dictionary source file
# Carlo Jose Mediarito - debugging of the program logic
# Vince Delos Santos - debugging of the program logic
# Karlo Tablang - interface sample codes
# Peter Burgos - sample documentation

import random

file = open("dictio.txt")

dictio = [line.strip() for line in file]

file.close()

# This function initializes the WORD HUNT game mode.
def unscrambler():

	# Variables used for the entirety of the game mode:
	score = 0
	total = 0
	attempts = 3
	words = []
	position = []
	final = []
	scorewords = []
	finalstring = []
	correct = []
	wrong = []
	check = ""

	# This dictionary serves as the basis for the scrabble points of each letter.
	scrabble = {"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "h":4, "i":1,
				"j":8, "k":5, "l":1, "m":3, "n":1, "o":1, "p":3, "q":10, "r":1,
				"s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y": 4, "z":10}

	# This loop generates random integers which will serve as the position
	# of random words in the dictionary.
	for x in range(random.randint(1, 3)):
		k = random.randint(0, len(dictio)-1)
		# This condition makes sure that the integers won't have duplicates
		# to prevent duplicate words.
		if k not in position:
			position.append(k)
	# This loop adds the randomly generated words into a new list.
	for x in position:
		words.append(dictio[x])
	
	# This loop creates the shortest possible string of letters from
	# the list of randomly picked words from the dictionary.
	for word in words:
		for letter in word:
			if letter in finalstring:
				if word.count(letter) >= finalstring.count(letter):
					finalstring.append(letter * (word.count(letter) - finalstring.count(letter)))
			else: 
				finalstring.append(letter)

	rand0m = random.shuffle(finalstring)
	rand0m = "".join(finalstring)
	print("Input words found in:")

	# This loop iterates over the list of all dictionary words to
	# check if all their letters are in the random string of letters.
	for word in dictio:
		rand = list(rand0m)
		for letter in word:
			if letter in rand:
				check += letter
				rand.remove(letter)
		if check in dictio and check not in scorewords:
			scorewords.append(check)
		check = ""

	# This loop iterates over the words in the list of all possible words
	# and adds the scrabble points of each letter in each word to get the
	# highest possible score.
	for word in scorewords:
		for a in word:
			total += scrabble[a]

	# This loop makes the user input words until his/her score is equal to
	# the highest possible score. The loop will also break if s/he quits or
	# if s/he has used up all his lives.
	while True:
		if score == total:
			break
		elif attempts == 0:
			break
		else:
			print(rand0m)
			print()
			userinpt = input("INPUT A WORD: ")
			# This condition checks if the input is found in the list of
			# all possible words from the random string of letters.
			if userinpt in scorewords:
				if userinpt not in correct:
					correct.append(userinpt)
					for char in userinpt:
						score += scrabble[char]
			# This statement terminates the program.
			elif userinpt == "/quit":
				print("=" * 24)
				break
			# This statement shuffles the random string of letters.
			elif userinpt == "/shuffle":
				shuffle = "".join(random.sample(rand0m, len(rand0m)))
				rand0m = shuffle
				print("=" * 24)
				continue
			else:
				if userinpt not in wrong:
					wrong.append(userinpt)
					attempts -= 1
			print("=" * 24)
			print("Correct guesses:", " ".join(correct))
			print("Wrong guesses:", " ".join(wrong))
			print()
			print("SCORE: ", score, "/", total)
			print("LIVES LEFT: ", attempts, "/ 3")
			print("=" * 24)

	if score == total:
		print("CONGRATULATIONS! You won!")
		print("*** SCORE: ", score, "/", total, "***")
	else:
		missed = [word for word in scorewords if word not in correct]
		print("GAME OVER! :(")
		print("-" * 6)
		print("WORDS YOU MISSED:")
		print("-"*6)
		print("\n".join(sorted(missed)))
		print("-" * 6)
		print("*** SCORE: ", score, "/", total, "***")

# This function initializes the ANAGRAM SEARCH game mode.
def anagrams():

	# Variables used for the entirety of the game mode:
	attempts = 3
	points = 0
	anagram = []
	correct = []
	wrong = []
	rand0m = ""

	# This loop checks if there is more than 1 anagram of the randomly picked
	# word from the dictionary. If it only has itself as its anagram, the loop
	# continues, which makes the program generate another random integer to
	# pick another word.
	while True:
		# This loop generates a random integer.
		for x in range(1):
			k = random.randint(0, len(dictio)-1)

		# This function takes two strings as arguments and checks if they are anagrams of each other. 
		# First we take in two strings. Each string is made into a sorted list of their letters.
		# Then we check if both lists are equal to each other. 
		# The function will then return a value of True if it satisfies the statement.
		def is_anagram(str1, str2):
			list_str1 = list(str1)
			list_str1.sort()
			list_str2 = list(str2)
			list_str2.sort()
			return list_str1 == list_str2

		word = dictio[k]

		# This loop adds the anagrams of the word into a list, and removes
		# the given word.
		for words in dictio:
			if is_anagram(word, words):
				anagram.append(words)
		anagram.remove(word)

		# These conditions check if the loop should continue or not.
		if len(anagram) > 1:
			break
		else:
			anagram = []
			continue

	# This variable enumerates how many anagrams there are for the word given.
	# Gives the maximum score.
	total = len(anagram)

	# This statement checks if the user's input is an anagram of the given word
	# and if it is part of the dictionary.
	# This statement also checks if the user has already input the same answer.
	while True:
		if attempts == 0:
			break
		elif points == total:
			break
		else:
			print(word)
			print()
			userinpt = input("INPUT AN ANAGRAM OF THE WORD: ")
			if userinpt in anagram:
				if userinpt not in correct:  
					correct.append(userinpt) 
					print("CORRECT!")
					points += 1
			elif userinpt == "/quit":
				print("=" * 24)
				break
			elif userinpt == "/shuffle":
				word = "".join(random.sample(word, len(word)))
				print("=" * 24)
				continue
			else:
				if userinpt not in wrong:
					wrong.append(userinpt)
					print("WRONG!")
					attempts -= 1

		print("=" * 24)
		print("Correct answers:", " ".join(correct))
		print("Wrong answers:", " ".join(wrong))
		print("-")
		print("SCORE: ", points, "/", total)
		print("LIVES LEFT: ", attempts, "/ 3")
		print("=" * 24)

	if points == total:
		print("CONGRATULATIONS! You won!")
		print("*** SCORE: ", points, "/", total, "***")

	else:
		print("GAME OVER!")
		print("-" * 6)
		print("ANSWERS:")
		print("-" * 6)
		print("\n".join(anagram))
		print("-" * 6)
		print("*** SCORE: ", points, "/", total, "***")

### END OF PROGRAM ###