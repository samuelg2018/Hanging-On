def boot_main(window, pg):
    # Import background image
    bg = pg.image.load('Media/main_screen.jpg')

    clock = pg.time.Clock()

    # Main Menu Loop
    while True:
        # Local Keys
        for event in pg.event.get():
            # Closes game when close button is clicked
            if event.type == pg.QUIT:
                return False, "N/A"
            # Closes game with ESC key (27 means ESC)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return False, "N/A"
                else:
                    return True, "level_1"

        # Draws Background
        window.blit(bg, (0, 0))

        pg.display.update()
        clock.tick(30)

