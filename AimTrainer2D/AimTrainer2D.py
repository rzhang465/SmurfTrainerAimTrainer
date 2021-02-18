"""
2D Aim Trainer Game
"""
import os
import time
import random
import pygame

pygame.init()

# Load Images
TARGET = pygame.transform.scale(pygame.image.load(os.path.join("assets", "target.png")), (30, 30))
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (1920, 1080))
CROSSHAIR = pygame.transform.scale(pygame.image.load(os.path.join("assets", "crosshair.png")), (20, 20))
# Set Window Settings
WIDTH, HEIGHT = 1920, 1080
GAME = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Aim Trainer 2D")

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, window):
        GAME.blit(TARGET, (self.x, self.y))


class CHair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cd=0

    def draw(self, window):
        GAME.blit(CROSSHAIR, (self.x, self.y))

    def setX(self, x):
        self.x=x
    
    def setY(self, y):
        self.y=y

def main():

    score = 0 
    font = pygame.font.Font("freesansbold.ttf", 32)
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    targTime = pygame.time.Clock()
    p1=CHair(960, 540)
    targets = []

    def redraw_window():
        GAME.blit(BG, (0, 0))
        scoreval = font.render("Score: " + str(score), True, "black") 
        GAME.blit(scoreval, (50, 50))
        pygame.draw.rect(GAME, "black", (315, 170, 1280, 720), 3)
        for x in targets:
             x.draw(GAME)
        p1.draw(GAME)
        pygame.display.update()

    while run:
        pygame.mouse.set_visible(False)
        clock.tick(FPS)
        x, y = pygame.mouse.get_pos()
        p1.setX(x)
        p1.setY(y)
        if (len(targets)<1):          
            targets.append(Target(random.randint(500, 1300), random.randint(300, 700)))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in targets:
                    if ((x+10)<=(i.x+30) and (y+10)<=(i.y+30) and (x+10)>=i.x and (y+10)>=i.y):
                        targets.remove(i)
                        score+=100
                    else:
                        score-=20
        redraw_window() 
    pygame.quit()

main()
