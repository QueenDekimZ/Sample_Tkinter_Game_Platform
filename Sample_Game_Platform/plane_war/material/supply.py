import pygame
from random import *

MAINFILE_PATH = "plane_war/material/"

# 超级子弹
class Bullet_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super(Bullet_Supply, self).__init__()
        
        self.image = pygame.image.load(MAINFILE_PATH+'images/bullet_supply.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = \
        randint(0, self.width - self.rect.width), -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = \
        randint(0, self.width - self.rect.width), -100

# 清图炸弹
class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super(Bomb_Supply, self).__init__()
        
        self.image = pygame.image.load(MAINFILE_PATH+'images/bomb_supply.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
        self.speed = 5
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False

    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100

