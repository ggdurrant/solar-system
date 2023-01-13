import pygame
from settings import *
from universe import Universe


# method to run simulation
def main():

    # initialize pygame
    pygame.init()
    game_display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # setup universe with starting number of planets
    universe = Universe(8)

    # redraw the display and planets
    def redraw_window():
        # draw background
        game_display.fill(BLACK)

        # draw the planet or orbit for each planet in universe
        for planet in universe.planets:
            # planet.init_vel(-1,1)
            # planet.draw(game_display)
            planet.draw_orbit(game_display)
        # draw sun
        universe.draw_sun(game_display)

        #update display
        pygame.display.update()


    # main loop
    while running:
        clock.tick(FPS)
        redraw_window()

        # update graviational forces on planets each tick and move planets
        for planet in universe.planets:
            universe.update_gravity()
            planet.move()

        # if exited, quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # end game
    pygame.quit()
    quit()

if __name__ == "__main__":  
    main()