import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('300x300')

# 设置打印值的标签
var1 = tk.StringVar()
l = tk.Label(
    window,
    bg='yellow',
    width=10,
    textvariable=var1
)
l.pack()

# 打印功能echo函数
def print_selection():
    varlue = lb.get(lb.curselection()) # 获取光标当前所在列表值
    var1.set(varlue)

# 打印按钮
b1 = tk.Button(
    window,
    text='print selection',
    width=15,
    height=2,
    command=print_selection
)
b1.pack()

# 设置列表框和列表值
var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(
    window,
    listvariable=var2
)
#将列表插入列表框
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)
lb.delete(1) # 删除索引位1的列表，即第2个
lb.pack()

window.mainloop()