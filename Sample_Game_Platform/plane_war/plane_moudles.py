import random
import pickle
import pygame
from itertools import cycle

from Login_window import window_class

SCREEN_SIZE = (400, 700)
WHITE = (255,255,255)
ENEMY_SPEED = [[1, 3], [1, 3], [1, 2], [0, 3], [-1, 4], [-1, 2]]
ITER_ENEMY_SPEED = cycle(ENEMY_SPEED)
CREATE_ENEMY_EVENT = pygame.USEREVENT
CHANGE_SPEED = pygame.USEREVENT + 1
PLANE_ME_FIRE = pygame.USEREVENT + 2
FLAG = 0
FIRE_COOL = 0


class Plane(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=[0, 0], SCREEN=None):
        super(Plane, self).__init__()
        self.SCREEN = SCREEN
        self.SCREEN_RECT = SCREEN.get_rect()
        # 加载图像
        self.image = pygame.image.load(image_name).convert_alpha()
        self.width, self.height = self.image.get_size()
        if image_name == "dog2.png":
            self.width, self.height = self.width // 4, self.height // 4
            self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))

            # 设置尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed

    def update(self, *args):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        self.SCREEN.blit(self.image, self.rect)
        # self.me.rect = self.me.rect.move(self.me.speed[0], self.me.speed[1])
        # self.screen.blit(self.me.image, self.me.rect)
        # if self.width < 200 and self.height < 200:
        # self.width, self.height = self.width + self.speed // 2, self.height + self.speed
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))


class PlaneEnemy(Plane):
    def __init__(self, SCREEN=None):
        super(PlaneEnemy, self).__init__("dog2.png", SCREEN=SCREEN)
        # self.speed[1] = random.randint(1,3)
        # self.speed[0] = random.randint(-2, 2)
        self.rect.bottom = self.SCREEN_RECT.top
        max_x = self.SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        super().update()
        global FLAG
        FLAG += 1
        if FLAG % 500 == 0:
            self.speed = next(ITER_ENEMY_SPEED)
            # self.speed[1] = random.randint(1, 3)
            # self.speed[0] = random.randint(-2, 2)
        # 敌机飞出屏幕释放对象
        if self.rect.y >= self.SCREEN_RECT.height:
            print("敌机飞出屏幕。。。")
            self.kill()

        # 敌机碰到边界弹回
        if self.rect.left < 0 or self.rect.right > self.SCREEN_RECT.width:
            self.speed[0] = -self.speed[0]
            if self.rect.right > self.SCREEN_RECT.width and self.rect.right + self.speed[0] > self.SCREEN_RECT.right:
                self.speed[0] = -self.speed[0]

    def update_speed(self):
        pass


class PlaneMe(Plane):
    def __init__(self, SCREEN=None, bullets_group=None):
        super(PlaneMe, self).__init__("plane_war/material/images/me1.png", SCREEN=SCREEN)
        self.speed = [0, 0]
        self.bullets_group = bullets_group
        # 设置初始位置
        # self.rect.centerx = self.SCREEN_RECT.centerx
        self.rect.x = self.SCREEN_RECT.width // 2
        self.rect.bottom = (self.SCREEN_RECT.height - self.SCREEN_RECT.y) // 2

    def update(self, *args):
        super().update()
        # 判断我机是否触碰边界
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.SCREEN_RECT.right:
            self.rect.right = self.SCREEN_RECT.right
        if self.rect.bottom > self.SCREEN_RECT.bottom + 30:
            self.rect.bottom = self.SCREEN_RECT.bottom + 30
        if self.rect.top < self.SCREEN_RECT.top:
            self.rect.top = self.SCREEN_RECT.top

    def fire(self):
        print("fire")
        # 创建子弹精灵
        self.bullet = Bullet(self.SCREEN)
        self.bullet.rect.bottom = self.rect.y - 3
        self.bullet.rect.x = (self.rect.right + self.rect.left) // 2

        self.bullets_group.add(self.bullet)


class Background(Plane):
    def __init__(self, SCREEN=None, is_alter=False):
        super(Background, self).__init__("plane_war/material/images/background.png", SCREEN=SCREEN)

        # 判断是否是交替图像，如果是，需要设置初始位置
        if is_alter:
            self.rect.y = -self.rect.height

    def update(self, *args):
        # 默认在垂直方向移动
        self.rect = self.rect.move(0, 1)
        self.SCREEN.blit(self.image, self.rect)
        # 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= self.SCREEN_RECT.height:
            self.rect.y = -self.SCREEN_RECT.height


class Bullet(Plane):
    def __init__(self, SCREEN=None):
        super(Bullet, self).__init__("plane_war/material/images/bullet1.png", SCREEN=SCREEN)
        self.speed = [0, -4]

    def update(self, *args):
        super().update()

        # 判断子弹是否撞击，如果是，释放精灵对象
        if self.rect.bottom < 0:
            self.kill()


class PlaneGame(object):
    def __init__(self, USER=None):
        # 用户
        self.USER = USER
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # 计分
        self.count = 0
        # 加载分数图
        self.number = [pygame.image.load('plane_war/material/images/0.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/1.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/2.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/3.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/4.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/5.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/6.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/7.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/8.png').convert_alpha(),
                       pygame.image.load('plane_war/material/images/9.png').convert_alpha()]
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 创建敌机精灵和精灵组
        self.__create_enemy_planes()
        # 创建我机精灵和精灵组
        self.__create_bullet()
        self.__create_me_plane()
        # 创建背景精灵和精灵组
        self.__create_background()
        # 创建敌机生成定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CHANGE_SPEED, 2500)
        # 游戏启动
        self.start_game()

    def __create_enemy_planes(self):
        self.enemy4 = PlaneEnemy(self.screen)
        self.enemy_group = pygame.sprite.Group(self.enemy4)

    def __create_me_plane(self):
        self.me = PlaneMe(self.screen, self.bullets_group)
        self.me_group = pygame.sprite.Group(self.me)

    def __create_background(self):
        # 创建背景精灵和精灵组
        bg1 = Background(self.screen)
        bg2 = Background(self.screen, True)
        self.background_group = pygame.sprite.Group(bg1, bg2)

    def __create_bullet(self):
        self.bullets_group = pygame.sprite.Group()

    def start_game(self):
        while True:
            # IO事件监听处理
            self.__event_detector()
            # 碰撞事件监听处理
            self.__collision_detector()
            # 更新精灵组
            self.__update_sprities()
            # 显示分数
            self.showScore()
            # 更新显示
            pygame.display.update()

    def __event_detector(self):
        global FIRE_COOL
        KEY_PRESSED = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场。。。")
                self.enemy_group.add(PlaneEnemy(self.screen))
            # elif event.type == CHANGE_SPEED:
            #     self.enemy_group. = next(ITER_ENEMY_SPEED)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # 按ESC退出
                    pygame.quit()
                    StartGui(self.USER)
                    return

        if KEY_PRESSED[pygame.K_UP]:
            self.me.speed = [0, -2]
        elif KEY_PRESSED[pygame.K_DOWN]:
            self.me.speed = [0, 2]
        elif KEY_PRESSED[pygame.K_LEFT]:
            self.me.speed = [-2, 0]
        elif KEY_PRESSED[pygame.K_RIGHT]:
            self.me.speed = [2, 0]
        elif KEY_PRESSED[pygame.K_a]:
            FIRE_COOL += 1
            if FIRE_COOL % 3 == 0:
                FIRE_COOL = 0
                self.me.fire()
        else:
            self.me.speed = [0, 0]
        # self.me.rect = self.me.rect.move(self.me.speed[0], self.me.speed[1])
        # self.screen.blit(self.me.image, self.me.rect)
        # elif KEY_PRESSED[pygame.K_UP]:
        #     print("up")
        # elif KEY_PRESSED[pygame.K_DOWN]:
        #     print("down")

        # elif KEY_PRESSED[pygame.K_LEFT]:
        #     print("left")
        #     self.me.speed = 2
        #
        # elif KEY_PRESSED[pygame.K_RIGHT]:
        #     print("right")
        #     self.me.speed = -2
        # else:
        #     self.me.speed = 0
        self.__collision_detector()

    def showScore(self):
        # 拆分数字
        scoreDigits = [int(x) for x in list(str(self.count))]
        # 计算数字总宽度
        totalWidth = 0
        for digit in scoreDigits:
            totalWidth += self.number[digit].get_rect().width
        # 居中摆放
        score_x_position = (self.screen.get_rect().width - totalWidth) // 2
        score_y_position = int(0.2 * self.screen.get_rect().height)
        # 刷新图
        for digit in scoreDigits:
            self.screen.blit(self.number[digit], (score_x_position, score_y_position))
            score_x_position += self.number[digit].get_rect().width

    def __collision_detector(self):
        self.clock.tick(60)
        # 子弹组和敌机组间的碰撞检测
        enemyp_list = pygame.sprite.groupcollide(self.me.bullets_group, self.enemy_group, dokilla=True, dokillb=False)
        if enemyp_list:
            for shoted_enemy in enemyp_list:
                # self.bullets_group.clear(surface=)
                for enemy in enemyp_list[shoted_enemy]:
                    enemy.kill()
                shoted_enemy.kill()
                self.count += 1
        enemy_list = pygame.sprite.spritecollide(self.me, self.enemy_group, dokill=True)
        if len(enemy_list) > 0:
            self.me.kill()
            self.__game_over()

    # def mount(self, *args):
    #     self.count += 1

    def __update_sprities(self):
        # 让敌机组调用 update 和 draw 方法
        self.__update_background()
        # 让背景组调用 update 和 draw 方法
        self.__update_enemy_planes_group()
        # 让我机组调用 update 和 draw 方法
        self.__update_me_plane_group()
        # 让我机子弹组调用 update 和 draw 方法
        self.__update_bullets()

    def __update_enemy_planes_group(self):
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    def __update_me_plane_group(self):
        self.me_group.update()
        self.me_group.draw(self.screen)

    def __update_background(self):
        self.background_group.update()
        self.background_group.draw(self.screen)

    def __update_bullets(self):
        self.bullets_group.update()
        self.bullets_group.draw(self.screen)

    def __game_over(self):
        scoreDic = {self.USER: self.count}
        try:
            with open('score.pkl', 'rb') as score_file:
                while True:
                    try:
                        users_info = pickle.load(score_file)
                        # 已有用户名记录，比较分数大小存较大一个
                        if self.USER in users_info:
                            if self.count > users_info[self.USER]:
                                with open('score.pkl', 'ab') as file:
                                    users_info[self.USER] = self.count
                        # 没有用户名记录，追加写记录
                        else:
                            with open('score.pkl', 'ab') as file:
                                pickle.dump(scoreDic, file)
                    except EOFError:
                        break
                # users_info = pickle.load(score_file)
                # # 已有用户名记录，比较分数大小存较大一个
                # if self.USER in users_info:
                #     if self.count > users_info[self.USER]:
                #         with open('score.pkl', 'ab') as file:
                #             users_info[self.USER] = self.count
                # # 没有用户名记录，追加写记录
                # else:
                #     with open('score.pkl', 'ab') as file:
                #         pickle.dump(scoreDic, file)
        # 没有文件直接追加写
        except FileNotFoundError:
            with open('score.pkl', 'ab') as file:
                pickle.dump(scoreDic, file)
        # 退出游戏，重新进入开始界面
        pygame.quit()
        StartGui(self.USER)


class StartGui(pygame.sprite.Sprite):
    def __init__(self, USER=None):
        # 用户
        self.USER = USER
        # 创建开始窗口
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.screen.fill([255, 255, 255])  # 用白色填充窗口
        KEY_PRESSED = pygame.key.get_pressed()

        self.button_start = pygame.image.load("plane_war/material/images/gamestart.png").convert_alpha()
        self.button_rank = pygame.image.load("plane_war/material/images/gamerank.png").convert_alpha()
        self.button_exit = pygame.image.load("plane_war/material/images/gameexit.png").convert_alpha()
        self.screen.blit(self.button_start, [50, 100])
        self.screen.blit(self.button_rank, [50, 160])
        self.screen.blit(self.button_exit, [50, 220])

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 < event.pos[0] < 50 + self.button_start.get_rect().width and 100 < event.pos[1] < 100 + self.button_start.get_rect().height:
                        GAME = PlaneGame(self.USER)
                    elif 50 < event.pos[0] < 50 + self.button_rank.get_rect().width and 160 < event.pos[1] < 160 + self.button_rank.get_rect().height:
                        self.__show_score_function()
                    elif 50 < event.pos[0] < 50 + self.button_exit.get_rect().width and 220 < event.pos[1] < 220 + self.button_exit.get_rect().height:
                        pygame.quit()
                        window_class.GameWindow(self.USER)
        # GAME = PlaneGame()

    def __show_score_function(self):
        try:
            with open('score.pkl', 'rb') as score_file:
                score_list = []
                while True:
                    try:
                        score_info = pickle.load(score_file)
                        for single in score_info:
                        # print(single, " ", score_info(single))
                            score_list.append(single+"            "+str(score_info[single]))
                    except:
                        break
                pygame.quit()
                ScoreList(score_list)
                    # StartGui(self.USER)

        except FileNotFoundError:
            self.message_diaplay()

            # score_info2 = unpicker.load()
        StartGui(self.USER)
    def __show_score(self):
        pass

class ScoreList(StartGui):
    def __init__(self, score_list=["无历史记录"]):
        pygame.init()
        self.score_list = score_list
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.screen.fill([0, 0, 0])  # 用黑色填充窗口
        for single in range(len(score_list)):
            self.message_diaplay(score_list[single], 120, 30*single + 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # 按ESC退出
                        pygame.quit()
                        return

    def message_diaplay(self, text="无历史记录", positionX=20, positionY=20):
        largeText = pygame.font.Font('plane_war/material/font/font.ttf', 15)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (positionX, positionY)
        # TextRect.center = ((self.screen.get_rect().width / 2), (self.screen.get_rect().height / 2))
        self.screen.blit(TextSurf, TextRect)
        pygame.display.flip()



    def text_objects(self, text, font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()




