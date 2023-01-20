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
    universe = Universe(3)
    universe.add_planet(WIDTH/2, 100, 1, .25, 5, 5, RED)
    universe.add_planet(WIDTH/2, HEIGHT-200, -3.1, -.35, 5, 8, GREEN)
    universe.add_planet(600, HEIGHT/2, 0, -4, 6, 10, BLUE)


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


    tick_counter = 0
    # main loop
    while running:
        if not SIMULATE:
            clock.tick(FPS)
            redraw_window()
        else:
            clock.tick(FPS)
            if tick_counter % 50 == 0:
                print(tick_counter)
                redraw_window()
            tick_counter += 1


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