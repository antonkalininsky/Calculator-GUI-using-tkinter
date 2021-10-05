from tkinter import *


class CalcUI(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def clicked(self, oper, in1, in2):
        if in1 == '' or in2 == '':
            buf = 'you have empty entries!'
        else:
            if oper == '+':
                buf = float(in1) + float(in2)
            elif oper == '-':
                buf = float(in1) - float(in2)
            elif oper == '*':
                buf = float(in1) * float(in2)
            elif oper == '/':
                if in2 == '0':
                    buf = 'cant div 0'
                else:
                    buf = float(in1) / float(in2)
            else:
                buf = 'error!'
        self.lblR.configure(text=buf)

    def initUI(self):
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
        btn1 = Button(frameOperations, text='+', command=lambda: self.clicked('+', txt1In.get(), txt2In.get()))
        btn2 = Button(frameOperations, text='-', command=lambda: self.clicked('-', txt1In.get(), txt2In.get()))
        btn3 = Button(frameOperations, text='*', command=lambda: self.clicked('*', txt1In.get(), txt2In.get()))
        btn4 = Button(frameOperations, text='/', command=lambda: self.clicked('/', txt1In.get(), txt2In.get()))
        # result elements
        lblR1 = Label(frameResult, text='result:')
        self.lblR = Label(frameResult, text='xxx')
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
        self.lblR.pack(side=TOP)


window = Tk()
window.title('calc lmao')
window.geometry('500x500')
calc1 = CalcUI()
window.mainloop()
