import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

tk.Label(window, text='on the window').pack()

frm = tk.Frame(window)
frm.pack()

# 设置窗口左右框架
frm_l = tk.Frame(frm, )
frm_r = tk.Frame(frm, )
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r1').pack()


window.mainloop()