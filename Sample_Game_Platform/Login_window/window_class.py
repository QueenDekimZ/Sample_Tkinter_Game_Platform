import sys

import tkinter as tk
from tkinter import messagebox
import pickle
import pygame

from flappy_bird import gesture_bird
from Login_window.modules import get_window_position
from flappy_bird.ball_game_test import ball_game_mouse_event
from plane_war import plane_moudles
from plane_war.material import main as main_plane
sys.setrecursionlimit(1000000)

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
        self.image_file = tk.PhotoImage(file='Login_window/images/welcome.gif')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.pack(side='top')

        # user information
        tk.Label(self, text='用户名:').place(x=50, y=150)
        tk.Label(self, text='密码:').place(x=50, y=190)

        # username entry
        self.var_usr_name = tk.StringVar()
        # self.var_usr_name.set('example@python.com', )
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
        self.mainloop()

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
                self.USER = usr_name
                tk.messagebox.showinfo(title='Welcome', message='欢迎来到大冰桑游戏平台, 玛斯塔 ' + usr_name)
                self.btn_game_window = tk.Button(self, width=11, text='进入游戏仓库', command=self.game_window)
                self.btn_game_window.place(x=300, y=240)
            else:
                tk.messagebox.showerror(message='您输入的用户名或密码不正确!')
        else:
            is_sign_up = tk.messagebox.askyesno(title='Welcome', message='该用户名还未注册，现在需要注册吗?')
            if is_sign_up:
                self.usr_sign_up()
            else:
                pass


    # sign up window
    def usr_sign_up(self):
        # global su_win_width
        # global su_win_height

        self.window_sign_up = tk.Toplevel(self)
        self.su_win_pos = get_window_position(self.su_win_width, self.su_win_height)
        self.window_sign_up.geometry(f'{self.su_win_width}x{self.su_win_height}+{self.su_win_pos[0]}+{self.su_win_pos[1]}')
        self.window_sign_up.title('Sign Up Window')

        self.new_name = tk.StringVar()
        # self.new_name.set('example@python.com')
        tk.Label(self.window_sign_up, text='用户名:').place(x=10, y=10)
        self.entry_new_name = tk.Entry(self.window_sign_up, textvariable=self.new_name)
        self.entry_new_name.place(x=150, y=10)

        self.new_pwd = tk.StringVar()
        tk.Label(self.window_sign_up, text='密码:').place(x=10, y=50)
        self.entry_new_pwd = tk.Entry(self.window_sign_up, textvariable=self.new_pwd, show='*')
        self.entry_new_pwd.place(x=150, y=50)

        self.new_pwd_confirm = tk.StringVar()
        tk.Label(self.window_sign_up, text='确认密码:').place(x=10, y=90)
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
            tk.messagebox.showerror(title='注册失败', message='该用户名已有用户创建。')
        elif np == None:
            tk.messagebox.showerror(title='注册失败', message='密码不能为空。')
        elif len(np) < 6:
            tk.messagebox.showerror(title='注册失败', message='密码至少得6位。')
        elif np != npc:
            tk.messagebox.showerror(title='注册失败', message='两次密码不一致。')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo(title='注册成功', message='恭喜成功创建用户！')
            self.window_sign_up.destroy()
            return
        self.window_sign_up.destroy()
        self.usr_sign_up()

    def game_window(self):
        self.destroy()
        GameWindow(self.USER)


# game seclection window
class GameWindow(tk.Tk, object):
    def __init__(self, USER="default"):
        super(GameWindow, self).__init__()
        self.select_win_width, self.select_win_height = 200, 500  # game selection window
        self.USER = USER
        # global select_win_width
        # global select_win_height
        # game_select_window = tk.Toplevel(window)
        self.select_win_pos = get_window_position(self.select_win_width, self.select_win_height)
        self.geometry(f'{self.select_win_width}x{self.select_win_height}+{self.select_win_pos[0]}+{self.select_win_pos[1]}')
        self.title('Game selection Window')

        dogb_ball_btn = tk.Button(self, width=20, text='DogB Ball', command=self.start_game1)
        dogb_ball_btn.place(x=20, y=30)
        dogb_flappy_btn = tk.Button(self, width=20, text='Flappy BogB', command=self.start_game2)
        dogb_flappy_btn.place(x=20, y=60)
        dogb_war_btn = tk.Button(self, width=20, text='BogB War', command=self.start_game3)
        dogb_war_btn.place(x=20, y=90)
        plane_war_btn = tk.Button(self, width=20, text='Plane War', command=self.start_game4)
        plane_war_btn.place(x=20, y=120)

        log_out_btn = tk.Button(self, width=10, text='退出登录', command=self.log_out)
        log_out_btn.place(x=60, y=460)

    # game body 1
    def start_game1(self):
        self.destroy()
        ball_game_mouse_event.main()
        GameWindow(self.USER)

    # game body 2
    def start_game2(self):
        self.destroy()
        gesture_bird.body()
        GameWindow(self.USER)

    # game body 3
    def start_game3(self):
        self.destroy()
        GAME3 = plane_moudles.StartGui(self.USER)
        GameWindow(self.USER)

    # game body 4
    def start_game4(self):
        self.destroy()
        main_plane.run(self.USER)
        GameWindow(self.USER)

    # log out
    def log_out(self):
        self.destroy()
        GamePlatform()
# if __name__ == '__main__':
#     window = GamePlatform()
#     window.mainloop()