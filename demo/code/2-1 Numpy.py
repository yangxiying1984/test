# -*- coding: utf-8 -*
from tkinter import *
#创建窗口
root = Tk()
#窗口标题
root.title("中英互译")
#窗口大小
root.geometry('370x100')
#窗口位置
root.geometry('+500+300')
#标签控件
lable = Label(root,text ='输入要翻译的文字:')
#标签定位
lable.grid()

lable1 = Label(root,text ='翻译之后的结果:')
lable1.grid()

#输入控件
entry = Entry(root,font = ('微软雅黑',15))
entry.grid()
#显示窗口  消息循环
root.mainloop()