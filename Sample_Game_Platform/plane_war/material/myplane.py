import pygame

MAINFILE_PATH = "plane_war/material/"

class MyPlane(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        super(MyPlane, self).__init__()

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
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.speed = 10

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.active = True
        self.invincible = True
