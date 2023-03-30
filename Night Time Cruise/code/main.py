# imports
import pygame, sys
pygame.init()
pygame.mixer.init()

# create screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Night Time Cruise :) ')

# background
bg = pygame.image.load('../images/background.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_scale = pygame.transform.smoothscale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
# used to get width of bg helps to move image in screen.blit
bg_width = bg.get_width()

# car
flipped_car = pygame.image.load('../images/car.png').convert_alpha()
car = pygame.transform.flip(flipped_car, True, False)
car_scale = pygame.transform.smoothscale(car, (200, 100))

# create frame rate
FPS = 60
clock = pygame.time.Clock()

# sound
main_fx = pygame.mixer.Sound('../sounds/journey-end.mp3')

# set speed of images to 0
bg_x = 0
car_x = 0

# event handler
run = True
while run:
    # sets frame rate
    clock.tick(FPS)
    main_fx.play()
    # sets background image to move from left to right
    screen.blit(bg, (bg_x % bg_width - bg_width, 0))
    # finishes up after first blit to keep image going endlessly after reaching Screen width
    # these blit codes are what keeps background looping
    screen.blit(bg, (bg_x % bg_width, 0))
    # background speed
    bg_x -= 2
    # set car and speed
    screen.blit(car_scale, (car_x, 600))
    car_x += 0.01
    # if car leaves screen width reset position
    if car_x > SCREEN_WIDTH:
        car_x = 0
    # event ran if you quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # updates display
    pygame.display.update()

# quit pygame
pygame.quit()
sys.exit()