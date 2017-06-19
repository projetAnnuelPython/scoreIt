from model.User import User
import tkinter as tk;
from tkinter import *
from database.databaseConnection import SqlDbConnection
import pymysql
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



import matplotlib.pyplot as plt

LARGE_FONT = ("Verdana", 22)


class App(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.current_user = None
        self.users = {}
        self.db_user = None
        self.db_password = None
        self.db_name = None
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.Frames = {}
        self.create_window()

    def set_db_connection_credentials(self, settings):
        self.db_user = settings['sql']['login']
        self.db_password = settings['sql']['password']
        self.db_name = settings['sql']['database_name']

    def set_connection(self):
        # create connexion
        connection = pymysql.Connect(user=self.db_user, passwd=self.db_password, database=self.db_name, autocommit=True)
        connection.commit()
        return connection
        connection = SqlDbConnection()
        return connection

    def find_user(self, email, password):
        connection = self.set_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email="%s" AND password="%s" ' % (email, password))
        row = cursor.fetchone()
        self.current_user = User(row[0], row[1], row[2], row[3], row[4], row[5])
        print(self.current_user.name)

    def find_all_users(self):
        connection = self.set_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        for row in cursor.fetchall():
            user = User(row[0], row[1], row[2], row[3], row[4], row[5])
            self.users[user.name] = user

    def create_window(self):
        self.home = Home(self)
        self.Frames['current'] = self.home
        self.home.pack(side="top")
        self.home.tkraise()

    def show_frame(self):
        self.Frames['current'].destroy()
        user_view = user_profile(self)
        self.Frames['current'] = user_view
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
        login_entry.insert(END, 'fode@fode.fr')
        login_entry.pack(pady=10, padx=10)

        password_label = tk.Label(self, text="Mot de passe", font=LARGE_FONT)
        password_label.pack(pady=10, padx=10)

        self.password = StringVar()
        password_entry = tk.Entry(self, textvariable=self.password)
        password_entry.insert(END, 'score_it_1234')
        password_entry.pack()

        validate_button = Button(self, height=100, text="VALIDER", command=lambda: self.on_login(),
                                 relief="ridge", bg="#000fff000")
        validate_button.pack(fill=BOTH)

    def on_login(self):
        self.controller.find_user(self.login.get(), self.password.get())
        self.controller.find_all_users()
        self.controller.show_frame()


class user_profile(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller

        top_pane = PanedWindow()
        label_firstname = Label(top_pane, text=self.controller.current_user.name)
        top_pane.add(label_firstname)
        label_lastname = Label(top_pane, text="Nom")
        top_pane.add(label_lastname)

        top_pane.grid(row=0, column=0, rowspan=3, pady=20)

        mid_pane = PanedWindow()
        label_test = Label(mid_pane, text='Statistiques')
        mid_pane.add(label_test)

        #mid_pane.add(canvas)

        mid_pane.grid(row=3, column=15, columnspan=10, rowspan=10)

        mid_pane_right = PanedWindow()
        label_ranking = Label(mid_pane_right, text='Classement')
        mid_pane_right.add(label_ranking)
        mid_pane_right.grid(row=3, column=100, padx=120)

        name = ['-18', '18-25', '25-50', '50+']
        data = [5000, 26000, 21400, 12000]

        explode = (0, 0.15, 0, 0)
        plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
        plt.axis('equal')
        plt.show()


def draw_pie(self, pane):
        names = [20, 30]
        data = [20, 30]
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot(names, data)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        #pane.add(canvas)

        #explode = (0, 0)
        #plt.pie(data, explode=explode, labels=names, autopct='%1.1f%%', startangle=90, shadow=True)
        #plt.axis('equal')
        #plt.show()

        #pane.add(plt)

