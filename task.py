import pygame
import random
import math

max_x = 500
max_y = 500


class Shape:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def bounce_if_needed(self, xl, yt, xr, yb):
        if self.x > xr or self.x <= xl:
            self.dx = -self.dx

        if self.y > yb or self.y <= yt:
            self.dy = -self.dy

    def move(self):
        self.x += self.dx
        self.y += self.dy


class Circle(Shape):
    def __init__(self, x, y, dx, dy, color, radius):
        Shape.__init__(self, x, y, dx, dy, color)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Square(Shape):
    def __init__(self, x, y, dx, dy, color, edge_length):
        Shape.__init__(self, x, y, dx, dy, color)
        self.edge_length = edge_length

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.edge_length, self.edge_length))
class Triangle(Shape):
    def __init__(self, x, y, dx, dy, color, size):
        Shape.__init__(self, x, y, dx, dy, color)
        self.size = size

    def draw(self, screen):
        
        point1 = (self.x, self.y - self.size)  # Top point
        point2 = (self.x - self.size, self.y + self.size)  # Bottom left
        point3 = (self.x + self.size, self.y + self.size)  # Bottom right
        
        pygame.draw.polygon(screen, self.color, [point1, point2, point3])

# BombCircle class (spiky circle)
class BombCircle(Shape):
    def __init__(self, x, y, dx, dy, color, radius, spikes=8):
        Shape.__init__(self, x, y, dx, dy, color)
        self.radius = radius
        self.spikes = spikes

    def draw(self, screen):
        points = []
        angle_step = 360 / (self.spikes * 2)

        for i in range(self.spikes * 2):
            angle = i * angle_step
            radian = math.radians(angle)
            if i % 2 == 0:
                r = self.radius * 1.5  # Longer spikes
            else:
                r = self.radius  # Inner points

            px = int(self.x + r * math.cos(radian))
            py = int(self.y + r * math.sin(radian))
            points.append((px, py))

        pygame.draw.polygon(screen, self.color, points)
#creating the shape
N = 20
avail_colors = ["red", "green", "blue"]
shapes = []
# its for the circle
for i in range(int(N/2)):
    col = random.randint(0, len(avail_colors) - 1)
    rad = random.randint(10, 30)
    speed_x = random.randint(-2, 2)
    speed_y = random.randint(-2, 2)
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    shapes.append(Circle(x, y, speed_x, speed_y, avail_colors[col], rad))
#its for the square
for i in range(N - int(N/2)):
    col = random.randint(0, len(avail_colors) - 1)
    edge_len = random.randint(10, 30)
    speed_x = random.randint(-2, 2)
    speed_y = random.randint(-2, 2)
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    shapes.append(Square(x, y, speed_x, speed_y, avail_colors[col], edge_len))
#for my spikey bomb
for i in range(N - int(2 * (N / 3))):  # Remaining shapes as BombCircles
    col = random.randint(0, len(avail_colors) - 1)
    rad = random.randint(10, 20)
    speed_x = random.randint(-2, 2)
    speed_y = random.randint(-2, 2)
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    shapes.append(BombCircle(x, y, speed_x, speed_y, avail_colors[col], rad, spikes=8))
for i in range(N // 4):  # Generate some triangles
    col = random.randint(0, len(avail_colors) - 1)
    size = random.randint(10, 30)
    speed_x = random.randint(-2, 2)
    speed_y = random.randint(-2, 2)
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    shapes.append(Triangle(x, y, speed_x, speed_y, avail_colors[col], size))

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
    screen.fill("yellow")

    for shape in shapes:
        shape.draw(screen)
        # pygame.draw.circle(screen, shape.color, (shape.x, shape.y), shape.radius)
        shape.move()
        shape.bounce_if_needed(0, 0, max_x, max_y)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()