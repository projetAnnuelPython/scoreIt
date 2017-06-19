from view.Home import Home
from view.UserProfile import UserProfile
from model.User import User
import tkinter as tk;
from tkinter import *
from database.databaseConnection import SqlDbConnection
import pymysql
import matplotlib
matplotlib.use('TkAgg')



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
        self.current_user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    def find_all_users(self):
        connection = self.set_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        for row in cursor.fetchall():
            user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            self.users[user.name] = user

    def create_window(self):
        self.home = Home(self)
        self.Frames['current'] = self.home
        self.home.pack(side="top")
        self.home.tkraise()

    def show_frame(self):
        self.Frames['current'].destroy()
        user_view = UserProfile(self)
        self.Frames['current'] = user_view
        user_view.tkraise()

    def go_play(self):
        print('Hello')
