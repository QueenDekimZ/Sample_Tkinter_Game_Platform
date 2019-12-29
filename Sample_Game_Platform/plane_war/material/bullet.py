import pygame

MAINFILE_PATH = "plane_war/material/"

class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Bullet1, self).__init__()

        self.image = pygame.image.load(MAINFILE_PATH+"images/My_zidan.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Bullet2, self).__init__()

        self.image = pygame.image.load(MAINFILE_PATH+"images/My_zidan.png").convert_alpha()
        self.width, self.height = self.image.get_size()
        self.width, self.height = self.width * 4, self.height * 4
        self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 14
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True