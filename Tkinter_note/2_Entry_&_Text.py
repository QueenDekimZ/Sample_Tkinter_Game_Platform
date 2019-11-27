import tkinter as tk
# from itertools import cycle

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

# dogb = ['d','o','g','b']
# it = cycle(dogb)
# 输入框
# e = tk.Entry(window, show=next(it)) # show=None
e  = tk.Entry(window, show='*')
e.pack()

#功能echo函数
def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    t.insert(2.2, var)

# 插入到显示框光标所在位置
b1 = tk.Button(
    window,
    text='insert point',
    width=15,
    height=2,
    command=insert_point
)
b1.pack()

# 插入显示框文本末
b2 = tk.Button(
    window,
    text='insert end',
    width=15,
    height=2,
    command=insert_end
)
b2.pack()

# 显示框
t = tk.Text(window, height=2)
t.pack()

# t.insert(2.2, var)
# 插入到第2行第3位

window.mainloop()