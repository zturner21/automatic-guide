import sys 
import pygame 
from settings import Settings
from ship import Ship
import game_ability 

'''
Notes-

problems->  Every library that I made had a problem where it wouldnt import the function to the code saying it was not a member.
This problem was fixed my me restarting my computer but I had to do it everytime I ran the game in order for it to work.
'''

#shout out MR.COZORT for the ideas and code

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Sad Boi Alien Game") 
    #creating the object
    ship = Ship(screen)
  
    #background color
    bg_color = ( 200, 200, 200)
    screen.fill(bg_color)
   
#this is my first attempt at making a spaceship
    # class spaceship:
    #     def __init__(self):
    #         self.image = pygame.Surface((30, 40))
    #         self.image.fill(WHITE)
    #         self.rect = self.image.get_rect()
    #         self.rect.center = (WIDTH / 12, HEIGHT /12)
    #         self.vx = 0
    #         self.vy = 0
    #         self.falling = False

    #game loop
    while True: 
        game_ability.check_events(ship)
        game_ability.check_events()
        game_ability.update_screen(ai_settings, screen, ship)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #keys being pressed and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

    
run_game()