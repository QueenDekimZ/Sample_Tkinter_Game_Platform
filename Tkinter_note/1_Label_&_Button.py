import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x100')


var = tk.StringVar()
l = tk.Label(
    window,
    textvariable=var,
    bg='green',
    font=('Arial',12),
    width=15,
    height=2
)
l.pack()
# l.place()

on_hit = False
def hit_dogb():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("TK is dogb's father")
    else:
        on_hit = False
        var.set('')
b = tk.Button(
    window,
    text='hit dogb',
    width=15,
    height=2,
    command=hit_dogb
)
b.pack()

window.mainloop()