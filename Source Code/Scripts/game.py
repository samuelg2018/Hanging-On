from random import randint
from Scripts.boxes import TextBox
from Scripts.result import game_over_screen, win

def right_letter():
	pass

def boot_game(window, pg):

	# Load background images
	sky = pg.image.load("Media/Background/sky.png")

	sea = []
	for frame in range(1, 41):
	    sea.append(pg.image.load(f"Media/Background/{frame}.png"))

	# Load Font
	font_import = pg.font.Font("media/font_bold.TTF", 43)
	game_txt = font_import.render("GUESS A LETTER", 1, (60, 60, 60))

	# Import shark images
	shark = pg.image.load("Media/Scene/Shark.png")

	# Import character images
	man = pg.image.load("Media/Scene/Man.png")

	# Import balloons 
	b_red = pg.image.load("Media/Scene/Red.png")
	b_blue = pg.image.load("Media/Scene/Blue.png")
	b_yellow = pg.image.load("Media/Scene/Yellow.png")
	b_black = pg.image.load("Media/Scene/Black.png")
	b_pink = pg.image.load("Media/Scene/Pink.png")
	b_green = pg.image.load("Media/Scene/Green.png")

	# Import Sounds
	wrong_sound = pg.mixer.Sound('Media/Sound/wrong.wav')
	right_sound = pg.mixer.Sound('Media/Sound/right.wav')

	# General Variables
	clock = pg.time.Clock()
	frame = 0
	loopcount = 0
	chances = 6
	game_over = False
	empty_letters = []
	decoded = []
	height = 0
	letter_position = []
	wrong_guesses = []
	guess = []
	letters = {}
	wrong_letters = {}
	right_count = 0

	# Import fonts for every letter
	for letter in range(26):
		letters[chr(65 + letter)] = font_import.render(chr(65 + letter), 1, (60, 60, 60))

	for w_letter in range(26):
		wrong_letters[chr(65 + w_letter)] = font_import.render(chr(65 + w_letter), 1, (220, 20, 60))

	# Main Loop
	while True:

		right = False
		instances = 0

		if chances > 0:
			for event in pg.event.get():
				# Closes Windows With Red X Button
				if event.type == pg.QUIT:
					return False, "N/A"
				elif event.type == pg.KEYDOWN:
					# If the key pressed is a letter
					if pg.key.name(event.key).isalpha():

						guess_copy = guess.copy()

						for letter in range(len(word)):
							if word[letter] == pg.key.name(event.key):
								right_sound.play()
								letter_position.append(letter)
								guess.append((pg.key.name(event.key)).upper())
								right = True
								right_count += 1
								instances += 1

						if not right:
							wrong_sound.play()
							if (pg.key.name(event.key)).upper() not in wrong_guesses:
								wrong_guesses.append((pg.key.name(event.key)).upper())
								chances -= 1
						
						if len(guess_copy) != len(guess) and guess[-1] in guess_copy:
							right_count -= instances				
							
			# Draw scene
			window.blit(sky, (0, 0))
			window.blit(sea[frame], (0, 460))
			window.blit(shark, (563, 530))
			window.blit(game_txt, (480, 10))

			# Decode words file
			if loopcount == 0:
				file = open("Media/words.en", "r")
				words = file.readlines()
				file.close()

				# Delete \n from every line
				for word in range(len(words)):
					if words[word][-1] == "\n":
						words[word] = words[word][:-1]

				for word in words:
					final = ""

					for letter in word.split(" ")[:-1]:
						final += chr(int(letter))

					decoded.append(final)

				# Get random word 
				randWord = randint(1, 213)
				word = decoded[randWord]
				print(word, len(word))

				# Draw empty boxes
				for i in range(len(word)):
					empty_letters.append(TextBox(window, pg, 250 + (80 * i)))
					
			for j in empty_letters:
				j.draw()

			# If 1 or more right guesses, draw them on top of corresponding text box 
			if guess:
				for key in range(len(guess)):
					empty_letters[letter_position[key]].draw_letters(guess[key])

			# Balloons animation position
			if loopcount % 60 < 30:
				height += ((loopcount % 60) ** 0.1 - 2).real
			else:
				height -= ((loopcount % 60 - 30) ** 0.1 - 2).real

			# Draw balloons
			if chances == 6:
				window.blit(b_black, (595, 140 + height))
				window.blit(b_blue, (610, 155 + height))
				window.blit(b_green, (558, 155 + height))
				window.blit(b_red, (592, 175 + height))
				window.blit(b_pink, (610, 180 + height))
				window.blit(b_yellow, (562, 180 + height))
			elif chances == 5:
				window.blit(b_black, (595, 140 + height))
				window.blit(b_blue, (610, 155 + height))
				window.blit(b_green, (558, 155 + height))
				window.blit(b_red, (592, 175 + height))
				window.blit(b_pink, (610, 180 + height))
			elif chances == 4:
				window.blit(b_black, (595, 140 + height))
				window.blit(b_blue, (610, 155 + height))
				window.blit(b_green, (558, 155 + height))
				window.blit(b_red, (592, 175 + height))
			elif chances == 3:
				window.blit(b_black, (595, 140 + height))
				window.blit(b_blue, (610, 155 + height))
				window.blit(b_green, (558, 155 + height))
			elif chances == 2:
				window.blit(b_black, (595, 140 + height))
				window.blit(b_blue, (610, 155 + height))
			elif chances == 1:
				window.blit(b_black, (595, 140 + height))
			else:
				game_over = True

			# Draw Character
			window.blit(man, (604, 300 + height))

			# Draw Wrong guesses
			if wrong_guesses:
				for key in range(len(wrong_guesses)):
					window.blit(wrong_letters[wrong_guesses[key]], (480 + (key * 60), 420))

			# If player wins
			if right_count == len(word):
				# Take screenshot
				pg.image.save(window, "Media/Scene/screenshot.png")
				# Win screen
				win(window, pg)
				return True, "main_menu"

			if frame < 39 and loopcount % 2 == 0:
				frame += 1
			elif frame >= 39:
				frame = 0

			loopcount += 1
			pg.display.update()
			clock.tick(30)

		else:
			# Take screenshot
			pg.image.save(window, "Media/Scene/screenshot.png")
			# Game Over screen
			game_over_screen(window, pg)


			return True, "main_menu"
