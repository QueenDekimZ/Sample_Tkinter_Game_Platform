import sys

import tkinter as tk
from tkinter import messagebox
import pickle
import pygame

from flappy_bird import gesture_bird
from modules import get_window_position

class GamePlatform(tk.Tk):
    def __init__(self):
        self.win_width, self.win_height = 450, 300  # login in window
        self.su_win_width, self.su_win_height = 350, 200  # sign up window
        self.select_win_width, self.select_win_height = 200, 500  # game selection window
        self.win_pos = get_window_position(win_width, win_height)  # for window's center position

        # window = tk.Tk()
        # window.title('DogB War')
        # window.geometry(f'{win_width}x{win_height}+{win_pos[0]}+{win_pos[1]}')
        self.title('DogB War')
        self.geometry(f'{win_width}x{win_height}+{win_pos[0]}+{win_pos[1]}')

        # welcome image
        self.canvas = tk.Canvas(window, height=200, width=500)
        self.image_file = tk.PhotoImage(file='images/welcome.gif')
        self.image = canvas.create_image(0, 0, anchor='nw', image=image_file)
        self.canvas.pack(side='top')

        # user information
        tk.Label(window, text='Username:').place(x=50, y=150)
        tk.Label(window, text='Password:').place(x=50, y=190)

        # username entry
        self.var_usr_name = tk.StringVar()
        self.var_usr_name.set('example@python.com', )
        self.entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
        self.entry_usr_name.place(x=160, y=150)

        # password entry
        var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=160, y=190)

    # login in logical function
    def usr_login_in():
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
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
                btn_game_window = tk.Button(window, width=8, text='进入游戏', command=game_window)
                btn_game_window.place(x=300, y=240)
            else:
                tk.messagebox.showerror(message='Your password is wrong, Please check and try again!')
        else:
            is_sign_up = tk.messagebox.askyesno(title='Welcome', message='You have not sign up yet. Sign up now?')
            if is_sign_up:
                usr_sign_up()
            else:
                window.quit()


    # sign up window
    def usr_sign_up():
        global su_win_width
        global su_win_height

        # sign up logical function
        def sign_to_db():
            nn = new_name.get()
            np = new_pwd.get()
            npc = new_pwd_confirm.get()
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
                window_sign_up.destroy()
                return
            usr_sign_up()

        window_sign_up = tk.Toplevel(window)
        su_win_pos = get_window_position(su_win_width, su_win_height)
        window_sign_up.geometry(f'{su_win_width}x{su_win_height}+{su_win_pos[0]}+{su_win_pos[1]}')
        window_sign_up.title('Sign Up Window')

        new_name = tk.StringVar()
        new_name.set('example@python.com')
        tk.Label(window_sign_up, text='Username:').place(x=10, y=10)
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
        entry_new_name.place(x=150, y=10)

        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
        entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_new_pwd.place(x=150, y=50)

        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='Confirm password:').place(x=10, y=90)
        entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_new_pwd_confirm.place(x=150, y=90)

        btn_confirm_sign_up = tk.Button(window_sign_up, width=8, text='注册', command=sign_to_db)
        btn_confirm_sign_up.place(x=150, y=130)

    # game body 1
    def start_game1():
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
    def start_game2():
        window.destroy()
        gesture_bird.body()

    # game seclection window
    def game_window():
        global select_win_width
        global select_win_height
        window.destroy()
        # game_select_window = tk.Toplevel(window)
        game_select_window = tk.Tk()
        select_win_pos = get_window_position(select_win_width, select_win_height)
        game_select_window.geometry(f'{select_win_width}x{select_win_height}+{select_win_pos[0]}+{select_win_pos[1]}')
        game_select_window.title('Game selection Window')

        dogb_war_btn = tk.Button(game_select_window, width=20, text='DogB War', command=start_game1)
        dogb_war_btn.place(x=20, y=30)
        dogb_flappy_btn = tk.Button(game_select_window, width=20, text='Flappy BogB', command=start_game2)
        dogb_flappy_btn.place(x=20, y=60)

if __name__ == '__main__':
    # login in and sign up button
    btn_login_in = tk.Button(window, width=8, text='登录', command=usr_login_in)
    btn_login_in.place(x=100, y=240)
    btn_sign_up = tk.Button(window, width=8, text='注册', command=usr_sign_up)
    btn_sign_up.place(x=200, y=240)
    # btn_sign_up = tk.Button(window, text='进入游戏', command=start_game)
    # btn_sign_up.place(x=300, y=240)

    window.resizable(False, False)  # 窗口大小不可变

    window.mainloop()