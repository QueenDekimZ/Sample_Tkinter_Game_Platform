import pygame

from plane_war import plane_class


GAME = plane_class.PlaneGame()

# screen = pygame.display.set_mode((400, 700))

# bg = pygame.image.load("material/images/background.png")
# screen.blit(bg, (0, 0))
# pygame.display.update()

# 创建敌机精灵和精灵组
# enemy1 = plane_class.PlaneEnemy("material/images/enemy1.png", 1, screen)
# enemy2 = plane_class.PlaneEnemy("material/images/enemy2.png", 2, screen)
# enemy4 = plane_class.PlaneEnemy("../dog2.png", 2, screen)
# enemy3 = plane_class.PlaneEnemy("material/images/enemy3_n1.png", 3, screen)
#
# enemy1.rect.x = 20
# enemy2.rect.x = 30
# enemy3.rect.x = 40
# enemy4.rect.x = 200

# enemy_group = pygame.sprite.Group(enemy1, enemy2, enemy3, enemy4)

# clock = pygame.time.Clock()
# while True:
#     clock.tick(60)
#     screen.blit(bg, (0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
#     # 让敌机组调用 update 和 draw 方法
#     enemy_group.update()
#     enemy_group.draw(screen)
#
#
#     pygame.display.update()
