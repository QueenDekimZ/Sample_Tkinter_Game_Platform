import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

canvas = tk.Canvas(window, bg='blue', height=100, width=300)
image_file = tk.PhotoImage(file='logo1.png')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
# anchor: n w e s nw ne sw se center 设图片上某个位置的点为锚定点

x0, y0, x1, y1 = 50, 50, 80, 80
# 线
line = canvas.create_line(x0, y0, x1, y1)
# 圆形
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
# 扇形， start：开始角度，extent：逆时针旋转角度范围
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=90, extent=90)
# 矩形
rect1 = canvas.create_rectangle(100, 30, 100+20, 30+20, fill='green')
rect2 = canvas.create_rectangle(85, 47, 85+50, 47+3, fill='green')
canvas.create_text(110, 90, text='dogb', fill= 'green',)
canvas.pack()

def moveit():
    canvas.move(rect1, 0, 2)
    canvas.move(rect2, 0, 2)

b = tk.Button(window, text='move', command=moveit).pack()

tk.mainloop()