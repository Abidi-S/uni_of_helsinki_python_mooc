# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0,0,0))

height = 50
for i in range(10):
    width = 40 + (i * robot.get_width())/5
    for j in range(10):
        window.blit(robot, (width, height))
        width += robot.get_width()
    height += 20
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()