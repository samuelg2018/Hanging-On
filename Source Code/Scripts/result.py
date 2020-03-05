def game_over_screen(window, pg):

	lose_sound = pg.mixer.Sound('Media/Sound/game_over.wav')
	screenshot = pg.image.load('Media/Scene/screenshot.png')
	clock = pg.time.Clock()
	lose_font_import = pg.font.Font("media/font_bold.TTF", 60)
	text = lose_font_import.render("GAME OVER", True, (0, 0, 0))

	lose_sound.play()
	frame = 0

	while frame < 200:
		window.blit(screenshot, (0, 0))
		window.blit(text, (500, 320))
		frame += 1

		pg.display.update()
		clock.tick(30)
	

def win(window, pg):
	
	win_sound = pg.mixer.Sound('Media/Sound/win.wav')
	screenshot = pg.image.load('Media/Scene/screenshot.png')
	clock = pg.time.Clock()
	win_font_import = pg.font.Font("media/font_bold.TTF", 60)
	text = win_font_import.render("YOU WIN", True, (0, 0, 0))

	win_sound.play()
	frame = 0

	while frame < 220:
		window.blit(screenshot, (0, 0))
		window.blit(text, (550, 320))
		frame += 1

		pg.display.update()
		clock.tick(30)