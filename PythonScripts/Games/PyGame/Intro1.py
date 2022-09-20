import pygame   
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *




vertices = (
    (0, 2, 0),
    (-2 , 0, 0),
    (2, 0, 0),
    (0, 0, 2)
)

edges = (
    (0, 1)
)

surfaces = (
    (0, 1, 2)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (0, 0, 0)
)


def Triangle():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glRotatef(0, 0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Triangle()
        pygame.display.flip()
        pygame.time.wait(10)

main()
