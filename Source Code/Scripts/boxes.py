class TextBox:
	def __init__(self, window, pg, x):
		self.window = window
		self.pg = pg
		self.x = x
		self.box = pg.image.load('media/scene/Box.png')
		self.letters = {}
		self.letters_font_import = pg.font.Font("media/font_bold.TTF", 40)

		for letter in range(26):
			self.letters[chr(65 + letter)] = self.letters_font_import.render(chr(65 + letter), 1, (0, 0, 0))

	def draw(self):
		self.window.blit(self.box, (self.x, 60))

	def draw_letters(self, guess):
		self.window.blit(self.letters[guess], (self.x + 20, 75))
		


	
	