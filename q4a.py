import pygame
pygame.init()

screen_width, screen_height = 500, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drawing Shapes in Pygame")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
       running = False

  screen.fill(white)
  pygame.draw.line(screen, red,(3, 200),(50, 50), 5)
  pygame.display.flip()

pygame.quit()