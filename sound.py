import pygame, sys
import numpy as np
import pygame.gfxdraw
from pygame.locals import *


CHERRYBLUE = (120, 171, 255)
CHERRYPINK = (255,129,171)
CHERRYPINKT = (255,54, 120)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
CHERRYPINKE = (255,209,255)
BGCOL = BLACK
pygame.init()

def drawLines(i):
    n = 70
    numLines = pygame.display.Info().current_w/n
    offset = (pygame.display.Info().current_w%n)
    # numLines = int(numLines)
    for j in xrange(numLines):
        pygame.gfxdraw.line(DISPLAYSURF, offset+j*n, 0, offset+j*n, pygame.display.Info().current_h, CHERRYPINKE)
def DrawCherryLoop(i, size, x = -1, y = -1):
    size = int(size)
    sizering = int(size/6)
    if x == -1:
        x = pygame.display.Info().current_w/2
    if y == -1:
        y = pygame.display.Info().current_h/2
    #middle ring
    pygame.gfxdraw.filled_circle(DISPLAYSURF, x, y, size, CHERRYBLUE)
    pygame.gfxdraw.filled_circle(DISPLAYSURF, x, y, size-int(size/50+1), BGCOL)
    #pink ring 1
    pygame.gfxdraw.filled_circle(DISPLAYSURF, int(x+size*np.cos(i+5*np.pi/3)), int(y+size*np.sin(i+5*np.pi/3)), sizering, CHERRYPINK)
    pygame.gfxdraw.filled_circle(DISPLAYSURF, int(x+size*np.cos(i+5*np.pi/3)), int(y+size*np.sin(i+5*np.pi/3)), sizering-int(size/50+1), BGCOL)
    #pink ring 2
    pygame.gfxdraw.filled_circle(DISPLAYSURF, int(x+size*np.cos(i+3*np.pi/3)), int(y+size*np.sin(i+3*np.pi/3)), sizering, CHERRYPINK)
    pygame.gfxdraw.filled_circle(DISPLAYSURF, int(x+size*np.cos(i+3*np.pi/3)), int(y+size*np.sin(i+3*np.pi/3)), sizering-int(size/50+1), BGCOL)
    #ping ring 3
    pygame.gfxdraw.filled_circle(DISPLAYSURF, int(x+size*np.cos(i+np.pi/3)), int(y+size*np.sin(i+np.pi/3)), sizering, CHERRYPINK)
    pygame.gfxdraw.filled_circle(DISPLAYSURF, int(x+size*np.cos(i+np.pi/3)), int(y+size*np.sin(i+np.pi/3)), sizering-int(size/50+1), BGCOL)

FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)
WHITE = (255, 255, 255)

# Music
# pygame.mixer.music.load("splash.mp3")
# pygame.mixer.music.play(-1, 0.0)
# pygame.mixer.music.set_volume(0.03)

# Font
# fontObj = pygame.font.Font('ace_futurism.ttf', 32)
# textSurfaceObj = fontObj.render('Cherry', True, CHERRYPINKT, BGCOL)
# textRectObj = textSurfaceObj.get_rect()
# textRectObj.center = (130, 130)

xsmo = pygame.display.Info().current_w/2
ysmo = pygame.display.Info().current_h/2
tick = 0
sizetick = 0
timekeep = 0
smoothingvar = .03
while True:
    DISPLAYSURF.fill(BGCOL)
    if timekeep < 600:
        if sizetick < 290:
            sizetick+= (290 - sizetick) * smoothingvar
        DrawCherryLoop(tick, int(sizetick+10))
    else:
        sizetick += (50 - sizetick) * smoothingvar
        xsmo += (100 - xsmo) * smoothingvar
        ysmo += (100 - ysmo) * smoothingvar
        DrawCherryLoop(tick, int(sizetick+10), int(xsmo), int(ysmo))
        # DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    # drawLines(tick)
    timekeep += 1
    tick+=.01
    pygame.display.update()
    fpsClock.tick(FPS)
