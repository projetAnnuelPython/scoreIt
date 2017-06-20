import tkinter as tk


class Root(tk.Tk):
    def __init__(self, *args, ** kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('500x300+300+40')
        self.title('SCORE IT')
        self.resizable(width=False, height=False)


