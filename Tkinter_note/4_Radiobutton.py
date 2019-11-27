import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('300x300')

# 设置打印值的标签
var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=30,
             text='empty')
l.pack()

# echo函数更改label设置，如打印值
def print_selection():
    l.config(text='You have selected ' + var.get())

# 定义3个单选按钮
r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()

window.mainloop()