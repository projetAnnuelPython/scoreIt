import tkinter as tk;
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')

LARGE_FONT = ("Verdana", 18)


class Home(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller

        login_label = tk.Label(self, text="Login", font=LARGE_FONT)
        login_label.pack(pady=10, padx=10)

        self.login = StringVar()
        login_entry = tk.Entry(self, textvariable=self.login)
        login_entry.insert(END, 'fode@fode.fr')
        login_entry.pack(pady=10, padx=10)

        password_label = tk.Label(self, text="Mot de passe", font=LARGE_FONT)
        password_label.pack(pady=10, padx=10)

        self.password = StringVar()
        password_entry = tk.Entry(self, textvariable=self.password)
        password_entry.insert(END, 'score_it_1234')
        password_entry.pack()

        self.error_text = StringVar()
        self.error_text.set('')
        self.error_label = Label(self, textvariable=self.error_text, font=LARGE_FONT, fg='red')
        self.error_label.pack()

        validate_button = Button(self, height=100, text="VALIDER", command=lambda: self.on_login(),
                                 relief="ridge", bg="#000fff000")
        validate_button.pack(fill=BOTH)


    def on_login(self):
        if self.login.get() and self.password.get():
            self.controller.find_user(self.login.get(), self.password.get())
            self.controller.find_all_users()
            self.controller.show_user_profile_screen()
        else:
            self.error_text.set('Identifiants incorrects')





