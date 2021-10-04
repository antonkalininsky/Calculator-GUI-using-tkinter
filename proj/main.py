from tkinter import *


def clicked(oper):
    if txt1.get() == '' or txt2.get() == '':
        buf = 'you have empty entries!'
    else:
        if oper == '+':
            buf = float(txt1.get()) + float(txt2.get())
        elif oper == '-':
            buf = float(txt1.get()) - float(txt2.get())
        elif oper == '*':
            buf = float(txt1.get()) * float(txt2.get())
        elif oper == '/':
            if txt2.get() == '0':
                buf = 'cant div 0'
            else:
                buf = float(txt1.get()) / float(txt2.get())
        else:
            buf = 'error!'
    lblR.configure(text=buf)


window = Tk()
window.title('calc lmao')
window.geometry('500x500')
lbl = Label(window, text="input 1")
lbl.grid(column=0, row=0)
txt1 = Entry(window, width=10)
txt1.grid(column=0, row=1)
lbl = Label(window, text="input 2")
lbl.grid(column=0, row=2)
txt2 = Entry(window, width=10)
txt2.grid(column=0, row=3)
btn1 = Button(window, text='+', command=lambda: clicked('+'))
btn2 = Button(window, text='-', command=lambda: clicked('-'))
btn3 = Button(window, text='*', command=lambda: clicked('*'))
btn4 = Button(window, text='/', command=lambda: clicked('/'))
btn1.grid(column=0, row=4)
btn2.grid(column=1, row=4)
btn3.grid(column=2, row=4)
btn4.grid(column=3, row=4)
lbl = Label(window, text='result')
lbl.grid(column=0, row=5)
global lblR
lblR = Label(window, text='xxx')
lblR.grid(column=0, row=6)
window.mainloop()
