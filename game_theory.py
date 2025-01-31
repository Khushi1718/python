# game =
# 1.game Loop:
#    event processing(start,end clode)
#    game play processing(gound ghum rha hai )
#    rendering(show it all in screnn)
# game loop mei jitne bhi repetion hote hai use frames bolte hai 
# 1sec mei kitne frame hue that is fps(frame per sec)

# delta time is last frame sei is frmae mei ane mei kya time laga 
import pygame
pygame.init()

# Create a game window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Test Window')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

pygame.quit()
