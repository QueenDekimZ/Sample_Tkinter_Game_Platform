import tkinter as tk
from tkinter import messagebox

from modules import get_window_position

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

def hit_me1():
    tk.messagebox.showinfo(title='Hi', message='hi dogb')  # 共3层messageinfo，第3层要重新引用
def hit_me2():
    tk.messagebox.showerror(title='error',message="dogb's existence is an error")
def hit_me3():
    tk.messagebox.showwarning(title='warning', message='climb dogb')
def hit_me4():
    print(tk.messagebox.askquestion(title='Hi', message='Is dogb still a noob?')) # return 'yes', 'no'
    # if return ==
def hit_me5():
    print(tk.messagebox.askyesno(title='Hi', message='Is dogb still a noob?')) # return 'True', 'False'
def hit_me6():
    print(tk.messagebox.askokcancel(title='Hi', message='Is dogb still a noob?')) # return 'True', 'False'
def hit_me7():
    print(tk.messagebox.askretrycancel(title='Hi', message='Is dogb still a noob?')) # return 'True', 'False'
def hit_me8():
    print(tk.messagebox.askyesnocancel(title='Hi', message='Is dogb still a noob?')) # return 'True', 'False', 'None'

tk.Button(window, text='show info', command=hit_me1).pack()
tk.Button(window, text='show error', command=hit_me2).pack()
tk.Button(window, text='show warning', command=hit_me3).pack()
tk.Button(window, text='ask question', command=hit_me4).pack()
tk.Button(window, text='ask yesno', command=hit_me5).pack()
tk.Button(window, text='ask okcancel', command=hit_me6).pack()
tk.Button(window, text='ask retrycancel', command=hit_me7).pack()
tk.Button(window, text='ask yesnocancel', command=hit_me8).pack()


window.mainloop()