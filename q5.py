import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


vertices = (
(0, 1, 0), 
(-1, -1, 0), 
(1, -1, 0), 
)

colors = (
(1, 0, 0), 
(1, 0, 0), 
(1, 0, 0), 
(0, 1, 0), 
(0, 0, 1), 
)

colors = (
(1, 0, 0), 
(0, 1, 0), 
(0, 0, 1), 
) 


def Triangle():
 glBegin(GL_TRIANGLES)
 glColor3f(1, 0, 0) #RED
 glVertex2f(0, 0.5)
 glColor3f(0, 1, 0) #Green
 glVertex2f(-0.5, -0.5)
 glColor3f(0, 0, 1) #BLUE
 glVertex2f(0.5, -0.5)
 glEnd()

def main():
 pygame.init()
 display = (800, 600)
 pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
 gluPerspective(45, display[0] / display[1], 0.1, 50.0)
# glTranslatef(0.0, 0.0, -5.0)
 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    quit()
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  Triangle()
  pygame.display.flip()
  pygame.time.wait(10)
main()  