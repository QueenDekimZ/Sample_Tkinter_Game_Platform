import sys

import tkinter as tk
from tkinter import messagebox
import pickle
import pygame

from flappy_bird import gesture_bird
from modules import get_window_position

class GamePlatform(tk.Tk, object):
    def __init__(self):
        super(GamePlatform, self).__init__()
        self.win_width, self.win_height = 450, 300  # login in window
        self.su_win_width, self.su_win_height = 350, 200  # sign up window
        self.select_win_width, self.select_win_height = 200, 500  # game selection window
        self.win_pos = get_window_position(self.win_width, self.win_height)  # for window's center position

        # window = tk.Tk()
        # window.title('DogB War')
        # window.geometry(f'{win_width}x{win_height}+{win_pos[0]}+{win_pos[1]}')
        self.title('DogB Game Platform')
        self.geometry(f'{self.win_width}x{self.win_height}+{self.win_pos[0]}+{self.win_pos[1]}')

        # welcome image
        self.canvas = tk.Canvas(self, height=200, width=500)
        self.image_file = tk.PhotoImage(file='images/welcome.gif')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.pack(side='top')

        # user information
        tk.Label(self, text='Username:').place(x=50, y=150)
        tk.Label(self, text='Password:').place(x=50, y=190)

        # username entry
        self.var_usr_name = tk.StringVar()
        self.var_usr_name.set('example@python.com', )
        self.entry_usr_name = tk.Entry(self, textvariable=self.var_usr_name)
        self.entry_usr_name.place(x=160, y=150)

        # password entry
        self.var_usr_pwd = tk.StringVar()
        self.entry_usr_pwd = tk.Entry(self, textvariable=self.var_usr_pwd, show='*')
        self.entry_usr_pwd.place(x=160, y=190)

        # login in and sign up button
        self.btn_login_in = tk.Button(self, width=8, text='登录', command=self.usr_login_in)
        self.btn_login_in.place(x=100, y=240)
        self.btn_sign_up = tk.Button(self, width=8, text='注册', command=self.usr_sign_up)
        self.btn_sign_up.place(x=200, y=240)
        # btn_sign_up = tk.Button(window, text='进入游戏', command=start_game)
        # btn_sign_up.place(x=300, y=240)
        self.resizable(False, False)  # 窗口大小不可变

    # login in logical function
    def usr_login_in(self):
        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                unpicker = pickle.Unpickler(usr_file)
                usrs_info = unpicker.load()
        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb') as usr_file:
                usr_admin = {'admin': 'admin'}
                pickle.dump(usr_admin, usr_file)
            with open('usrs_info.pickle', 'rb') as usr_file:
                unpicker = pickle.Unpickler(usr_file)
                usrs_info = unpicker.load()
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tk.messagebox.showinfo(title='Welcome', message='欢迎来到飞翔的大冰桑, 玛斯塔 ' + usr_name)
                self.btn_game_window = tk.Button(self, width=8, text='进入游戏', command=self.game_window)
                self.btn_game_window.place(x=300, y=240)
            else:
                tk.messagebox.showerror(message='Your password is wrong, Please check and try again!')
        else:
            is_sign_up = tk.messagebox.askyesno(title='Welcome', message='You have not sign up yet. Sign up now?')
            if is_sign_up:
                self.usr_sign_up()
            else:
                self.quit()


    # sign up window
    def usr_sign_up(self):
        # global su_win_width
        # global su_win_height

        self.window_sign_up = tk.Toplevel(self)
        self.su_win_pos = get_window_position(self.su_win_width, self.su_win_height)
        self.window_sign_up.geometry(f'{self.su_win_width}x{self.su_win_height}+{self.su_win_pos[0]}+{self.su_win_pos[1]}')
        self.window_sign_up.title('Sign Up Window')

        self.new_name = tk.StringVar()
        self.new_name.set('example@python.com')
        tk.Label(self.window_sign_up, text='Username:').place(x=10, y=10)
        self.entry_new_name = tk.Entry(self.window_sign_up, textvariable=self.new_name)
        self.entry_new_name.place(x=150, y=10)

        self.new_pwd = tk.StringVar()
        tk.Label(self.window_sign_up, text='Password:').place(x=10, y=50)
        self.entry_new_pwd = tk.Entry(self.window_sign_up, textvariable=self.new_pwd, show='*')
        self.entry_new_pwd.place(x=150, y=50)

        self.new_pwd_confirm = tk.StringVar()
        tk.Label(self.window_sign_up, text='Confirm password:').place(x=10, y=90)
        self.entry_new_pwd_confirm = tk.Entry(self.window_sign_up, textvariable=self.new_pwd_confirm, show='*')
        self.entry_new_pwd_confirm.place(x=150, y=90)

        self.btn_confirm_sign_up = tk.Button(self.window_sign_up, width=8, text='注册', command=self.sign_to_db)
        self.btn_confirm_sign_up.place(x=150, y=130)

        # sign up logical function
    def sign_to_db(self):

        nn = self.new_name.get()
        np = self.new_pwd.get()
        npc = self.new_pwd_confirm.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if nn in exist_usr_info:
            tk.messagebox.showerror(title='草', message='憨批，非要起跟别人一样的账户名？')
        elif np == None:
            tk.messagebox.showerror(title='草', message='憨批，密码不能为空你造马？')
        elif len(np) < 6:
            tk.messagebox.showerror(title='草', message='憨批，密码至少得6位你造马？')
        elif np != npc:
            tk.messagebox.showerror(title='草', message='憨批，重复密码都能写错？')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo(title='草', message='恭喜这个憨批，成功创建账户！')
            self.window_sign_up.destroy()
            return
        self.usr_sign_up()

    # game body 1
    def start_game1(self):
        # bg_size = width, height = 1000, 660
        pygame.init()  # 初始化pygame。启用Pygame必不可少的一步，在程序开始阶段执行
        vInfo = pygame.display.Info()
        bg_size = width, height = vInfo.current_w, vInfo.current_h
        # print(width,height)
        screen = pygame.display.set_mode(bg_size, pygame.FULLSCREEN)  # 创建屏幕对象（也即窗口对象）,分辨率1200*900
        # print(bg_size)
        # set_mode(r=(0,0),flags=0) flags用来显示类型，可用|组合使用
        # 常用pygame.RESIZABLE 窗口大小可调用   #要有尺寸变化的响应
        # pygame.NOFRAME 窗口没有边界显示    #增加退出方式
        # pygame.FULLSCREEN 窗口全屏显示    #分辨率对应问题

        speed = [1, 1]
        pygame.display.set_caption("Python壁球")  # 窗口标题
        bg_color = (230, 230, 230)  # 屏幕背景色
        ball = pygame.image.load('../dog2.png')
        ballrect = ball.get_rect()
        fps = 20000
        fclock = pygame.time.Clock()
        while True:  # 游戏主循环
            for event in pygame.event.get():  # 监视键盘和鼠标事件
                if event.type == pygame.QUIT:  # 关闭窗口的事件
                    sys.exit()  # 退出程序
                elif event.type == pygame.KEYDOWN:  # 键盘敲击事件 K_UP or K_DOWN or K_LEFT or K_RIGHT
                    if event.key == pygame.K_LEFT:
                        speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
                    elif event.key == pygame.K_RIGHT:
                        speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
                    elif event.key == pygame.K_DOWN:
                        speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
                    elif event.key == pygame.K_UP:
                        speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    bg_size = width, height = event.size[0], event.size[1]
                    screen = pygame.display.set_mode(bg_size, pygame.RESIZABLE)
            ballrect = ballrect.move(speed[0], speed[1])
            # print(abs(ballrect.right - ballrect.left))
            # print(abs(ballrect.top - ballrect.bottom))
            if ballrect.left <= 0 or ballrect.right >= width:
                speed[0] = -speed[0]
            if ballrect.top <= 0 or ballrect.bottom >= height:
                speed[1] = -speed[1]
            screen.fill(bg_color)  # 填充屏幕背景色
            screen.blit(ball, ballrect)
            pygame.display.update()  # 刷新屏幕
            fclock.tick(fps)  # 控制帧速度，即窗口刷新速度，每秒最大framerate次帧刷新

    # game body 2
    def start_game2(self):
        gesture_bird.body()

    # game seclection window
    def game_window(self):
        # global select_win_width
        # global select_win_height
        self.destroy()
        # game_select_window = tk.Toplevel(window)
        game_select_window = tk.Tk()
        self.select_win_pos = get_window_position(self.select_win_width, self.select_win_height)
        game_select_window.geometry(f'{self.select_win_width}x{self.select_win_height}+{self.select_win_pos[0]}+{self.select_win_pos[1]}')
        game_select_window.title('Game selection Window')

        dogb_war_btn = tk.Button(game_select_window, width=20, text='DogB War', command=self.start_game1)
        dogb_war_btn.place(x=20, y=30)
        dogb_flappy_btn = tk.Button(game_select_window, width=20, text='Flappy BogB', command=self.start_game2)
        dogb_flappy_btn.place(x=20, y=60)

if __name__ == '__main__':
    window = GamePlatform()
    window.mainloop()