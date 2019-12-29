import pygame

MAINFILE_PATH = "plane_war/material/"

class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position, screen):
        super(Bullet1, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(MAINFILE_PATH+"images/My_zidan.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.bottom < self.screen.get_rect().top:
            self.active = False
        else:
            self.rect.top -= self.speed


    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position, screen):
        super(Bullet2, self).__init__()
        self.screen = screen
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
        if self.rect.bottom < self.screen.get_rect().top:
            self.active = False
        else:
            self.rect.top -= self.speed

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True