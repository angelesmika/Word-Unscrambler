import engine

def home_screen():
	# This function prints the main menu / home screen of the game.
	print("\n" + ("=" * 30))
	print("     ___ __  __ ___ ___ ")
	print("    | __|  \/  | _ \_ _|")
	print("    | _|| |\/| |  _/| | ")
	print("    |___|_|  |_|_| |___|" + "\n")
	print("INSTRUCTIONS:")
	print("- To quit, type /quit.")
	print("- To shuffle, type /shuffle." + "\n")

def game():
	# This function makes the player choose a game mode.
	while True:
		print("CHOOSE A GAME MODE: ")
		print("1 - WORD HUNT")
		print("2 - ANAGRAM SEARCH")
		print("3 - QUIT" + "\n")

		mode = input("GAME MODE: ")

		print("=" * 30)

		if mode == "1" or mode == "2":
			break
		elif mode == "3":
			exit()
		else:
			print("INVALID GAME MODE!")
			print("=" * 30)
			continue

	if mode == "1":
		print("NOTE: Only words with 3-5 letters are counted! ;)")
		print()
		engine.unscrambler()
	else:
		engine.anagrams()