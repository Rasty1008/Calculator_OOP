from tkinter import*
from typing import Callable

class View:
    def __init__(self):
        self.root = Tk()
        self.equation = StringVar()

    def set_equation(self, value):
        self.equation.set(value)

    def setup_view(self, callback: Callable):
        calculation = Label(self.root, textvariable = self.equation)
        self.set_equation("0")
        calculation.grid(columnspan = 4)
        self.setup_buttons(callback)

    def setup_buttons(self, callback: Callable):
        button1 = Button(self.root, text = "1", command = lambda: callback("1"))
        button1.grid(row = 1, column = 0)

        button2 = Button(self.root, text = "2", command = lambda: callback("2"))
        button2.grid(row = 1, column = 1)

        button3 = Button(self.root, text = "3", command = lambda: callback("3"))
        button3.grid(row = 1, column = 2)

        button4 = Button(self.root, text = "4", command = lambda: callback("4"))
        button4.grid(row = 2, column = 0)

        button5 = Button(self.root, text = "5", command = lambda: callback("5"))
        button5.grid(row = 2, column = 1)

        button6 = Button(self.root, text = "6", command = lambda: callback("6"))
        button6.grid(row = 2, column = 2)

        button7 = Button(self.root, text = "7", command = lambda: callback("7"))
        button7.grid(row = 3, column = 0)

        button8 = Button(self.root, text = "8", command = lambda: callback("8"))
        button8.grid(row = 3, column = 1)

        button9 = Button(self.root, text = "9", command = lambda: callback("9"))
        button9.grid(row = 3, column = 2)

        button0 = Button(self.root, text = "0", command = lambda: callback("0"))
        button0.grid(row = 4, column = 0)

        button_plus = Button(self.root, text = "+", command = lambda: callback("+"))
        button_plus.grid(row = 1, column = 3)

        button_minus = Button(self.root, text = "-", command = lambda: callback("-"))
        button_minus.grid(row = 2, column = 3)

        button_multi = Button(self.root, text = "*", command = lambda: callback("*"))
        button_multi.grid(row = 3, column = 3)

        button_divide = Button(self.root, text = "/", command = lambda: callback("/"))
        button_divide.grid(row = 4, column = 3)

        button_equal = Button(self.root, text = "=", command = lambda: callback("="))
        button_equal.grid(row = 4, column = 2)

        button_clear = Button(self.root, text = "C", command = lambda: callback("C"))
        button_clear.grid(row = 4, column = 1)

    def start_main_loop(self):
        self.root.mainloop()

        