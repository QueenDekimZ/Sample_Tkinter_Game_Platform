import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('300x300')

# 设置打印值的标签
var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=30,  # width为字符长度
             text='empty')
l.pack()

# echo函数更改label设置，如打印值
def print_selection(v):
    l.config(text='You have selected ' + v)

# 设置滑动条
s = tk.Scale(window, label='try me', from_=5, to=11,
             orient=tk.HORIZONTAL,  # 方向为水平
             length=200,      # length为像素长度
             showvalue=1,     # 滑动块上方显示滑动条值
             tickinterval=2,   # 滑动条刻度间隔为2
             resolution=0.01,   # 精确单位到2位小数
             command=print_selection  # echo函数
)
s.pack()

window.mainloop()