import pygame as pg
from Scripts.main_menu import boot_main
from Scripts.game import boot_game

# Main
if __name__ == "__main__":
    # Window initialization
    pg.init()
    window = pg.display.set_mode((1280, 720))
    pg.display.set_caption("Hanging On")

    # Sequence Variables 
    running = True
    level = "main_menu"

    # Main Loop
    while running:
        # Scene Selkect
        if level == "main_menu":
            running, level = boot_main(window, pg)
        if level == "level_1":
            running, level = boot_game(window, pg)
    # Program Finalization 
    pg.quit()
