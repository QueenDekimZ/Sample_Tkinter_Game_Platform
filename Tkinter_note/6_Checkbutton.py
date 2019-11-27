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
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 1) & (var2.get() == 1):
        l.config(text='I love both')
    else:
        l.config(text='I do not love either')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)    # 选定该框，value置1，否则置0
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()

window.mainloop()