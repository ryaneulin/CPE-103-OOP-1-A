from tkinter import *

class MyWindow:
    def __init__(self, win):

    # BUTTON
        self.lbl1 = Label(win, text = 'First number')
        self.lbl2 = Label(win, text = 'Second number')
        self.lbl3 = Label(win, text = 'Result')
    # Text Box Size
        self.t1 = Entry(bd = 3)
        self.t2 = Entry()
        self.t3 = Entry()
    # Button size
        self.btn1 = Button(win, text = 'Add')
        self.btn2 = Button(win, text = 'Subtract')
        self.btn3 = Button(win, text = 'Multiply')
        self.btn4 = Button(win, text = 'Divide')
        self.lbl1.place(x=100, y=50)
        #self.btn5 = Button(win, text = 'Clear')
        #self.btn6 = Button(win, text = 'Delete')

    # Button place
        self.t1.place(x = 200, y = 50)
        self.lbl2.place(x = 100, y = 100)
        self.t2.place(x = 200, y = 100)

        self.btn1 = Button(win, text = 'Add', command = self.add)
        self.btn2 = Button(win, text = 'Subtract', command = self.sub)
        self.btn2.bind('<Button-1>',self.sub)
        self.btn3 = Button(win, text = 'Multiply', command = self.multiply)
        self.btn3.bind('<Button-2')
        self.btn4 = Button(win, text = 'Divide', command=self.divide)
        self.btn4.bind('<Button-3')
        self.btn5 = Button(win, text='Clear', command=self.clear)
        self.btn5.bind('<Button-3')
        self.btn6 = Button(win, text='Delete', command=self.delete)
        self.btn6.bind('<Button-3')

    # Button Size
        self.btn1.place(x = 100, y = 150)
        self.btn2.place(x = 160, y = 150)
        self.btn3.place(x = 250, y = 150)
        self.btn4.place(x = 350, y = 150)
        self.btn5.place(x = 140, y = 200)
        self.btn6.place(x = 300, y = 200 )
        self.lbl3.place(x = 100, y = 250)
        self.t3.place(x = 200, y = 250)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def multiply(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def divide(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))
    def clear(self):
        self.t3.delete(0, 'end')

    def delete(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')


window = Tk()
mywin = MyWindow(window)
window.title('MY PYTHON CALCULATOR')
window.geometry("500x400+10+10")
window.mainloop()
