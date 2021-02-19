"""
2D Aim Trainer Game
"""
import os
import time
import random
import pygame

pygame.init()

# Load Images
TARGET = pygame.transform.scale(pygame.image.load("o:/Coding_Projects/SmurfTrainerAimTrainer/AimTrainer2D/assets/target.png"), (30, 30))
BG = pygame.transform.scale(pygame.image.load("o:/Coding_Projects/SmurfTrainerAimTrainer/AimTrainer2D/assets/background.jpg"), (1920, 1080))
CROSSHAIR = pygame.transform.scale(pygame.image.load("o:/Coding_Projects/SmurfTrainerAimTrainer/AimTrainer2D/assets/crosshair.png"), (20, 20))
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

class Scene(object):
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

class GameScene(Scene):
        def __init__(self):
            super(GameScene, self).__init__()
            self.score=0
            self.targets=[]
            self.font = pygame.font.Font("freesansbold.ttf", 32)
            self.p1=CHair(960, 540)
            

        def render(self):
            GAME.blit(BG, (0, 0))
            scoreval = self.font.render("Score: " + str(self.score), True, "black") 
            GAME.blit(scoreval, (50, 50))
            pygame.draw.rect(GAME, "black", (315, 170, 1280, 720), 3)
            for x in self.targets:
                x.draw(GAME)
            self.p1.draw(GAME)
            pygame.display.update()


        def update(self):    
            x, y = pygame.mouse.get_pos()
            self.p1.setX(x)
            self.p1.setY(y)      
            if (len(self.targets)<1):          
                self.targets.append(Target(random.randint(500, 1300), random.randint(300, 700)))


        def handle_events(self, events):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for i in self.targets:
                        if ((x+10)<=(i.x+30) and (y+10)<=(i.y+30) and (x+10)>=i.x and (y+10)>=i.y):
                            self.targets.remove(i)
                            self.score+=100
                        else:
                            self.score-=20
                             

class TitleScene(Scene):

    def __init__(self):
        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont("freesansbold.ttf", 100)
        self.sfont = pygame.font.SysFont("freesansbold.ttf", 64)
        self.swap=False

    def render(self):
        GAME.blit(BG, (0, 0))
        text1 = self.font.render("Welcome to Aim Trainer", True, "black")
        text2 = self.sfont.render("> press space to start <", True, "black")
        GAME.blit(text1, (570, 370))
        GAME.blit(text2, (720, 540))
        pygame.display.update()


    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.swap=True

    

def main():

    run = True
    FPS = 60
    clock = pygame.time.Clock()
    scene = GameScene()
    title = TitleScene()

    while run:
        pygame.mouse.set_visible(False)

        clock.tick(FPS) 

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        if (title.swap==False):
            title.render()
            title.handle_events(events)
            if (title.swap==True):
                scene.update()
                scene.render()
                scene.handle_events(events)
        else :
            scene.update()
            scene.render()
            scene.handle_events(events)

    pygame.quit()

main()
