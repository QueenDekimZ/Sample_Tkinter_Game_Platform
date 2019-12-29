import pygame
from random import *

MAINFILE_PATH = "plane_war/material/"

class SmallEnemy(pygame.sprite.Sprite):
    energy = 1

    def __init__(self, bg_size):
        super(SmallEnemy, self).__init__()

        self.image = pygame.image.load(MAINFILE_PATH+'images/blow1.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(MAINFILE_PATH+'images/blow1_1.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH+'images/blow1_2.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow1_3.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow1_4.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow1_5.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow1_6.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow1_7.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow1_8.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow1_9.png').convert_alpha(),
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2
        self.reset()
        self.energy = SmallEnemy.energy
        self.hit = False
        

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)
        self.active = True
        self.energy = SmallEnemy.energy


class MidEnemy(pygame.sprite.Sprite):

    energy = 8

    def __init__(self, bg_size):
        super(MidEnemy, self).__init__()

        self.image = pygame.image.load(MAINFILE_PATH+'images/blow2.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(MAINFILE_PATH+'images/blow2_1.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow2_2.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow2_3.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow2_4.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow2_5.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow2_6.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow2_7.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow2_8.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow2_9.png').convert_alpha(),
        ])
        self.image_hit = pygame.image.load(MAINFILE_PATH+'images/blow2_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.reset()
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)
        self.active = True
        self.energy = MidEnemy.energy


class BigEnemy(pygame.sprite.Sprite):
    energy = 20

    def __init__(self, bg_size):
        super(BigEnemy, self).__init__()
        self.image = pygame.image.load(MAINFILE_PATH+'images/My_plane.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(MAINFILE_PATH+'images/blow3_1.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow3_2.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow3_3.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow3_4.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow3_5.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow3_6.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow3_7.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow3_8.png').convert_alpha(),
            pygame.image.load(MAINFILE_PATH + 'images/blow3_9.png').convert_alpha(),
            ])
        self.image_hit = pygame.image.load(MAINFILE_PATH+'images/blow3_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.appear = False
        self.reset()
        self.energy = BigEnemy.energy
        self.hit = False


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-20 * self.height, -10 * self.height)
        self.active = True
        self.energy = BigEnemy.energy
