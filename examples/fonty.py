
"""Here we load a .TTF font file, and display it in
a basic pygame window. It demonstrates several of the
Font object attributes. Nothing exciting in here, but
it makes a great example for basic window, event, and
font management."""


import pygame, pygame.font, os.path
import pygame.cursors
from pygame.locals import *


def main():
    #initialize
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.mouse.set_cursor(*pygame.cursors.diamond)

    #fill background
    screen.fill(screen.map_rgb((40, 40, 90)))
    pygame.display.flip()

    #load font, prepare values
    fontname = os.path.join('data', 'billbrdi.ttf')
    font = pygame.font.font(fontname, 80)
    text = 'Fonty'
    size = font.size(text)
    fg = (250, 240, 230)
    bg = (5, 5, 5)

    #no AA, no transparancy, normal
    ren = font.render(text, 0, fg, bg)
    screen.blit(ren, (10, 10))

    #no AA, transparancy, underline
    font.set_underline(1)
    ren = font.render(text, 0, fg)
    screen.blit(ren, (10, 20 + size[1]))
    font.set_underline(0)

    #AA, no transparancy, bold
    font.set_bold(1)
    ren = font.render(text, 1, fg, bg)
    screen.blit(ren, (20 + size[0], 10))
    font.set_bold(0)

    #AA, transparancy, italic
    font.set_italic(1)
    ren = font.render(text, 1, fg)
    screen.blit(ren, (20 + size[0], 20 + size[1]))
    font.set_italic(0)

    #show the surface and await user quit
    pygame.display.flip()
    while 1:
        #use event.wait to keep from polling 100% cpu
        if pygame.event.wait().type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
            break



if __name__ == '__main__': main()
    