import pygame

max_x = 500
max_y = 500

x = 10
y = 10

dx = 1
dy = 2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((max_x, max_y))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "yellow", (x, y), 10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    x += dx
    y += dy

    if x > max_x or x <= 0:
        dx = -dx

    if y > max_y or y <= 0:
        dy = -dy

    clock.tick(60)  # limits FPS to 60

pygame.quit()