import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
ball_radius = 15
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 4, 4

# Paddle properties
paddle_width, paddle_height = 100, 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_speed = 6

# Game loop
clock = pygame.time.Clock()

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and ball_y + ball_radius >= HEIGHT - paddle_height
    ):
        ball_dy = -ball_dy

    # Ball falls below paddle (game over)
    if ball_y + ball_radius > HEIGHT:
        print("Game Over!")
        running = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(
        screen, BLUE, (paddle_x, HEIGHT - paddle_height, paddle_width, paddle_height)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
