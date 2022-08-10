# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
# REWRITE
    x += velocity
    if velocity > 0 and x + robot.get_width() >= 640:
        x = 640 - robot.get_width()
        y += velocity

    if velocity > 0 and y + robot.get_height() >= 480:
        velocity = -velocity
        y = 480 - robot.get_height()

    if velocity < 0 and x <= 0:
        x = 0
        y += velocity

    if velocity < 0 and y <= 0:
        y = 0
        velocity = -velocity


    clock.tick(150)