
import pygame, pygame.mixer   # accesses pygame files
import sys      # to communicate with windows
import random, math


def textDraw(msgText, XYPosition, color):
    font = pygame.font.Font(fontName, 28)  # <<<<<<<< try changing the size
    text_surface = font.render(msgText, True, color)  # <<<<< try changing the color
    screen.blit(text_surface, XYPosition)  # <<<< try changing the position


def pythag(pX, pY, tX, tY):
    a = pX - tX
    b = pY - tY
    c = math.sqrt(a ** 2 + b ** 2)
    return c

# game setup ################ only runs once

pygame.init()   # starts the game engine
clock = pygame.time.Clock()     # creates clock to limit frames per second
FPS = 60  # sets max speed of min loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1000, 800  # sets size of screen/window
screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen
# set variables for colors RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
fontName = pygame.font.match_font('arial')
gameState = "splash"  # controls which state the games is in
# ADD CODE HERE

# game loop #################### runs 60 times a second!
while gameState != "exit":  # game loop - note: everything in the mainloop is indented

    for event in pygame.event.get():  # get user interaction
        if event.type == pygame.QUIT:  # tests if window X has been clicked
            gameState = "exit"  # causes exit of game loop
        if event.type == pygame.MOUSEBUTTONUP:
            fireLock = 0

    if gameState == "splash":
        screen.fill(white)
        textDraw("Click to begin", (SCREENWIDTH / 2 - 100, SCREENHEIGHT / 2), red)
        if pygame.mouse.get_pressed()[0]:
            gameState = "playing"
            startTime = pygame.time.get_ticks()  # stores current time
            # ADD CODE HERE

    elif gameState == "playing":
        screen.fill(black)
        # ADD CODE HERE

        textDraw("Time: " + str(pygame.time.get_ticks() - startTime), (SCREENWIDTH / 2 - 100, 70), green)
        if pygame.time.get_ticks() - startTime > 10000:  # change state after 10 seconds
            gameState = "gameOver"

    elif gameState == "gameOver":
        screen.fill(black)
        # ADD CODE HERE

        textDraw("Right click to play again", (400, 400), green)
        if pygame.mouse.get_pressed()[2]:
            gameState = "splash"

    pygame.display.flip()  # transfers virtual screen to human viable screen
    clock.tick(FPS)
    # your code ends here ###############################
    pygame.display.flip()  # transfers virtual screen to human viable screen
    clock.tick(FPS)  # limits loop cycles per second

# out of game loop ###############
print("The game has closed")
pygame.quit()   # stops the game engine
sys.exit()  # close windows window




