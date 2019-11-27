import tkinter as tk
from tkinter import messagebox
import pickle
import sys
from modules import get_window_position

win_width, win_height = 450, 300   # login in window
su_win_width, su_win_height = 350, 200   # sign up window
win_pos = get_window_position(win_width, win_height)   # for window's center position

window = tk.Tk()
window.title('DogB War')
window.geometry(f'{win_width}x{win_height}+{win_pos[0]}+{win_pos[1]}')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='images/welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='Username:').place(x=50, y=150)
tk.Label(window, text='Password:').place(x=50, y=190)

# username entry
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com',)
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)

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
            usr_admin = {'admin':'admin'}
            pickle.dump(usr_admin, usr_file)
        with open('usrs_info.pickle', 'rb') as usr_file:
            unpicker = pickle.Unpickler(usr_file)
            usrs_info = unpicker.load()
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='Welcome to DogB War, ' + usr_name)
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

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_db)
    btn_confirm_sign_up.place(x=150, y=130)

# login in and sign up button
btn_login_in = tk.Button(window, text='login in', command=usr_login_in)
btn_login_in.place(x=150, y=240)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=250, y=240)

window.resizable(False, False) # 窗口大小不可变

window.mainloop()