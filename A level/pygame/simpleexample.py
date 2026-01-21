#sprites
#Mr Reed
#OCt 2023

import random

# CONSTANTS
COL_WHITE = (255, 255, 255)
COL_BLACK = (0,0,0)
COL_BLUE = (0, 0, 255)

WINDOW_NAME = "Sprites - Mr Reed (c) 2023"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Import and initialize the pygame library
import pygame
pygame.init()

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
   K_UP,
   K_DOWN,
   K_LEFT,
   K_RIGHT,
   K_ESCAPE,
   KEYDOWN,
   QUIT,
)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

FRAME_RATE = 60
ENEMY_SPAWN_TIME = 100

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((100, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #screen is a "surface"
pygame.display.set_caption(WINDOW_NAME)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, ENEMY_SPAWN_TIME)

# Instantiate a player object
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Run until the user asks to quit
running = True
while running:

   # Did the user click the window close button?
   for event in pygame.event.get():
      if event.type == KEYDOWN:
         # Was it the Escape key? If so, stop the loop.
         if event.key == K_ESCAPE:
            running = False
            
      elif event.type == QUIT:
         running = False

      # Add a new enemy?
      elif event.type == ADDENEMY:
          # Create the new enemy and add it to sprite groups
          new_enemy = Enemy()
          enemies.add(new_enemy)
          all_sprites.add(new_enemy)

   # Get the set of keys pressed and check for user input
   pressed_keys = pygame.key.get_pressed()

   #tell the player object which keys are pressed in
   player.update(pressed_keys)

   # Update enemy position
   enemies.update()

   # Fill the background with white
   screen.fill(COL_BLACK)

   # Draw all sprites
   for entity in all_sprites:
       screen.blit(entity.surf, entity.rect)

   #position = (
   #    (SCREEN_WIDTH-player.surf.get_width())/2,
   #    (SCREEN_HEIGHT-player.surf.get_height())/2)

   #screen.blit(player.surf, position)
   screen.blit(player.surf, player.rect)


   # Flip the display
   pygame.display.flip()

   # Ensure program maintains a rate of 30 frames per second
   clock.tick(FRAME_RATE)

# Done! Time to quit.
pygame.quit()
