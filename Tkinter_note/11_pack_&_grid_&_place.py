import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

# tk.Label(window, text=1).pack(side='top')
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')

for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=30, pady=5, ipadx= 5,ipady=5)
# 1.row=x,column=y：将控件放在x行，y列的位置。
# 2.columnspan： 设置单元格横向跨越的列数，即控件占据的列数（宽度）； rowspan：设置单元格纵向跨越的行数，即控件占据的行数（高度）。
# 3.ipadx：设置控件里面水平方向空白区域大小； ipady：设置控件里面垂直方向空白区域大小；
#   padx：设置控件周围水平方向空白区域保留大小； pady：设置控件周围垂直方向空白区域保留大小；
# 4.sticky:默认的控件在窗口中的对齐方式是居中。可以使用sticky选项去指定对齐方式，
# 可以选择的值有：N/S/E/W，分别代表上对齐/下对齐/左对齐/右对齐，可以单独使用N/S/E/W，也可以上下和左右组合使用，达到不同的对齐效果

tk.Label(window, text=1).place(x=20, y=20, anchor='nw')   # anchor：label某个角设为锚定点
window.mainloop()