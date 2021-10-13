from tkinter import *


class CalcEasyUI(Frame):

    def __init__(self, win):
        super().__init__()
        self.initUI(win)

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
        if type(buf) is float:
            buf = round(buf, 3)

        self.lblR.configure(text=buf)

    def initUI(self, win):
        # frames creation
        frameInputs = Frame(win)
        frameOperations = Frame(win)
        frameResult = Frame(win)
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


class CalcButtonsUI(Frame):

    def __init__(self, win):
        super().__init__()
        self.initUI(win)

    class Message:
        text = str()
        isError = bool()
        isRslt = bool()

        def __init__(self):
            self.text = ''
            self.isError = False
            self.isRslt = False

        def sendStr(self, wid):
            wid.configure(text=self.text)

        def clearStr(self):
            self.text = ''

        def updateStr(self, oper):
            self.text += oper

        def click(self, oper, wid):
            if self.isRslt or self.isError:
                self.isRslt = False
                self.isError = False
                self.clearStr()
                self.sendStr(wid)
            if oper == 'C':
                self.clearStr()
            elif oper == '=':
                if self.text.count('+') + self.text.count('-') + self.text.count('*') + self.text.count('/') == 1:
                    if self.text.find('+') != -1:
                        buf = self.text.split('+')
                        op = 1
                    if self.text.find('-') != -1:
                        buf = self.text.split('-')
                        op = 2
                    if self.text.find('/') != -1:
                        buf = self.text.split('/')
                        op = 3
                    if self.text.find('*') != -1:
                        buf = self.text.split('*')
                        op = 4
                    if buf[0].count('.') <= 1 and buf[1].count('.') <= 1:
                        if op == 1:
                            self.text = float(buf[0]) + float(buf[1])
                        if op == 2:
                            self.text = float(buf[0]) - float(buf[1])
                        if op == 3:
                            if float(buf[1]) != 0:
                                self.text = float(buf[0]) / float(buf[1])
                            else:
                                self.text = 'ERROR'
                                self.isError = True
                        if op == 4:
                            self.text = float(buf[0]) * float(buf[1])
                        self.text = round(self.text, 3)
                        self.isRslt = True
                    else:
                        self.text = 'ERROR'
                        self.isError = True
                else:
                    self.text = 'ERROR'
                    self.isError = True
            else:
                self.updateStr(oper)
            self.sendStr(wid)

    def initUI(self, win):
        # creating frames
        frameInputs = Frame(win)
        frameScreen = Frame(win)
        # creating in\out unit
        inputStr = self.Message()
        # creating in\out window
        windowInOut = Label(frameScreen, height=2, width=28)
        windowInOut.pack(side=TOP, padx=2, pady=10)
        # creating buttons
        btnOpPlus = Button(frameInputs, text='+', height=2, width=5, command=lambda: inputStr.click('+', windowInOut))
        btnOpMin = Button(frameInputs, text='-', height=2, width=5, command=lambda: inputStr.click('-', windowInOut))
        btnOpMul = Button(frameInputs, text='*', height=2, width=5, command=lambda: inputStr.click('*', windowInOut))
        btnOpDiv = Button(frameInputs, text='/', height=2, width=5, command=lambda: inputStr.click('/', windowInOut))
        btnOpEqual = Button(frameInputs, text='=', height=6, width=5, command=lambda: inputStr.click('=', windowInOut))
        btnOpClr = Button(frameInputs, text='C', height=6, width=5, command=lambda: inputStr.click('C', windowInOut))
        btnNum0 = Button(frameInputs, text='0', height=2, width=14, command=lambda: inputStr.click('0', windowInOut))
        btnNum1 = Button(frameInputs, text='1', height=2, width=5, command=lambda: inputStr.click('1', windowInOut))
        btnNum2 = Button(frameInputs, text='2', height=2, width=5, command=lambda: inputStr.click('2', windowInOut))
        btnNum3 = Button(frameInputs, text='3', height=2, width=5, command=lambda: inputStr.click('3', windowInOut))
        btnNum4 = Button(frameInputs, text='4', height=2, width=5, command=lambda: inputStr.click('4', windowInOut))
        btnNum5 = Button(frameInputs, text='5', height=2, width=5, command=lambda: inputStr.click('5', windowInOut))
        btnNum6 = Button(frameInputs, text='6', height=2, width=5, command=lambda: inputStr.click('6', windowInOut))
        btnNum7 = Button(frameInputs, text='7', height=2, width=5, command=lambda: inputStr.click('7', windowInOut))
        btnNum8 = Button(frameInputs, text='8', height=2, width=5, command=lambda: inputStr.click('8', windowInOut))
        btnNum9 = Button(frameInputs, text='9', height=2, width=5, command=lambda: inputStr.click('9', windowInOut))
        btnPnt = Button(frameInputs, text='.', height=2, width=5, command=lambda: inputStr.click('.', windowInOut))
        # positioning buttons
        btnOpPlus.grid(row=0, column=0, sticky=W + S, padx=10, pady=10)
        btnOpMin.grid(row=0, column=1, sticky=W + S, padx=10, pady=10)
        btnOpMul.grid(row=0, column=2, sticky=W + S, padx=10, pady=10)
        btnOpDiv.grid(row=0, column=3, sticky=W + S, padx=10, pady=10)
        btnNum7.grid(row=1, column=0, sticky=W + S, padx=10, pady=10)
        btnNum8.grid(row=1, column=1, sticky=W + S, padx=10, pady=10)
        btnNum9.grid(row=1, column=2, sticky=W + S, padx=10, pady=10)
        btnOpEqual.grid(row=1, column=3, rowspan=2, sticky=W + S, padx=10, pady=10)
        btnNum4.grid(row=2, column=0, sticky=W + S, padx=10, pady=10)
        btnNum5.grid(row=2, column=1, sticky=W + S, padx=10, pady=10)
        btnNum6.grid(row=2, column=2, sticky=W + S, padx=10, pady=10)
        btnNum1.grid(row=3, column=0, sticky=W + S, padx=10, pady=10)
        btnNum2.grid(row=3, column=1, sticky=W + S, padx=10, pady=10)
        btnNum3.grid(row=3, column=2, sticky=W + S, padx=10, pady=10)
        btnOpClr.grid(row=3, column=3, rowspan=2, sticky=W + S, padx=10, pady=10)
        btnNum0.grid(row=4, column=0, columnspan=2, sticky=W + S, padx=10, pady=10)
        btnPnt.grid(row=4, column=2, sticky=W + S, padx=10, pady=10)
        # packing frames
        frameScreen.pack()
        frameInputs.pack()


window = Tk()
window.title('calc lmao')
window.geometry('500x500')
calc = CalcEasyUI(window)
calc2 = CalcButtonsUI(window)
window.mainloop()
