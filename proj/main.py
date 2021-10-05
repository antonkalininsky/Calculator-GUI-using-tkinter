from tkinter import *


def clicked(oper):
    if txt1In.get() == '' or txt2In.get() == '':
        buf = 'you have empty entries!'
    else:
        if oper == '+':
            buf = float(txt1In.get()) + float(txt2In.get())
        elif oper == '-':
            buf = float(txt1In.get()) - float(txt2In.get())
        elif oper == '*':
            buf = float(txt1In.get()) * float(txt2In.get())
        elif oper == '/':
            if txt2In.get() == '0':
                buf = 'cant div 0'
            else:
                buf = float(txt1In.get()) / float(txt2In.get())
        else:
            buf = 'error!'
    lblR.configure(text=buf)


window = Tk()
window.title('calc lmao')
window.geometry('500x500')
# frames creation
frameInputs = Frame(window)
frameOperations = Frame(window)
frameResult = Frame(window)
# input elements
lbl1In = Label(frameInputs, text="input 1:")
txt1In = Entry(frameInputs, width=10)
lbl2In = Label(frameInputs, text="input 2:")
txt2In = Entry(frameInputs, width=10)
# operations elements
lblOP = Label(frameOperations, text="operation:")
btn1 = Button(frameOperations, text='+', command=lambda: clicked('+'))
btn2 = Button(frameOperations, text='-', command=lambda: clicked('-'))
btn3 = Button(frameOperations, text='*', command=lambda: clicked('*'))
btn4 = Button(frameOperations, text='/', command=lambda: clicked('/'))
# result elements
lblR1 = Label(frameResult, text='result:')
lblR = Label(frameResult, text='xxx')
# final positioning
frameInputs.pack()
lbl1In.pack(side=TOP)
txt1In.pack(side=TOP)
lbl2In.pack(side=TOP)
txt2In.pack(side=TOP)
frameOperations.pack()
lblOP.pack(side=TOP, fill=X)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=LEFT)
frameResult.pack()
lblR1.pack(side=TOP)
lblR.pack(side=TOP)

window.mainloop()
