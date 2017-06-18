import tkinter as tk;
from tkinter import *
import os,sys


LARGE_FONT = ("Verdana", 22)


class App(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.Frames = {}
        self.create_window()

    def create_window(self):
        self.home = Home(self)
        self.Frames['current'] = self.home
        self.home.pack(side="top")
        self.home.tkraise()

    def show_frame(self):
        self.Frames['current'].destroy()
        user_view = user_profile(self)
        self.Frames['current'] = user_view
        user_view.pack(side="top")
        user_view.tkraise()


class Home(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller

        login_label = tk.Label(self, text="Login", font=LARGE_FONT)
        login_label.pack(pady=10, padx=10)

        self.login = StringVar()
        login_entry = tk.Entry(self, textvariable=self.login)
        login_entry.pack(pady=10, padx=10)

        password_label = tk.Label(self, text="Mot de passe", font=LARGE_FONT)
        password_label.pack(pady=10, padx=10)

        self.password = StringVar()
        password_entry = tk.Entry(self, textvariable=self.password)
        password_entry.pack()

        #button_image = image.open(file="/Users/fofofofodev/Desktop/ESGI3A/OUTILS DU DEVELOPPEUR /ProjetAnnuel/scoreIt/view/go.gif")
        validate_button = Button(self, height=100, text="VALIDER", command=lambda: self.on_login(),
                                 relief="ridge", bg="#000fff000")
        #validate_button.config(font=("Verdana", 20))
        validate_button.pack(fill=BOTH)

    def on_login(self):
        print("Login is {}".format(self.login.get()))
        print("password is {}".format(self.password.get()))


class user_profile(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller
        #back_button = tk.Button(self, text="RETOUR", width=10, command=controller.create_window())
        #back_button.pack()
        label = tk.Label(self, text="USER PROFILE!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
