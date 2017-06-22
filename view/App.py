from view.Playground import Playground
from view.Home import Home
from view.UserProfile import UserProfile
from model.User import User
import tkinter as tk
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
        self.show_home_screen()
        self.home = None

    def update_average(self):
        try:
            self.get_user_by_id()
            connection = self.set_connection()
            cursor = connection.cursor()
            cursor.execute('UPDATE users SET user_average="%s" WHERE user_id="%s"' % (self.current_user.update_user_average(), self.current_user.user_id))
            connection.commit()

        except pymysql.MySQLError as err:
            print('failed to update user_average. Error is {}'.format(err))

    def update_score(self, boolean):
        try:
            connection = self.set_connection()
            cursor = connection.cursor()
            if boolean:
                cursor.execute('UPDATE users SET score="%s" WHERE user_id="%s"' % ((self.current_user.score + 10), self.current_user.user_id))
            else:
                cursor.execute('UPDATE users SET score="%s" WHERE user_id="%s"' % (
                              (self.current_user.score - 10), self.current_user.user_id))
            connection.commit()

        except pymysql.MySQLError as error:
            print(error)

    def get_user_by_id(self):
        try:
            connection = self.set_connection()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE user_id="%s"' % self.current_user.user_id)
            row = cursor.fetchone()
            self.current_user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        except pymysql.MySQLError as error:
            print(error)

    def update_total_questions(self):
        try:
            connection = self.set_connection()
            cursor = connection.cursor()
            cursor.execute('UPDATE users SET total_questions = "%s" WHERE user_id="%s"'%((self.current_user.total_questions + 1), self.current_user.user_id))
            connection.commit()
        except pymysql.MySQLError as error:
            print('Failed to update total_questions. Error is {}'.format(error))

    def set_db_connection_credentials(self, settings):
        self.db_user = settings['sql']['login']
        self.db_password = settings['sql']['password']
        self.db_name = settings['sql']['database_name']

    # create connexion
    def set_connection(self):
        try:
            connection = pymysql.Connect(user=self.db_user, passwd=self.db_password, database=self.db_name, autocommit=True)
            connection.commit()
            return connection
        except pymysql.MySQLError as error:
            print('MySql connection failed. Error is {}'.format(error))

    def find_user(self, email, password):
        try:
            connection = self.set_connection()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users WHERE email="%s" AND password="%s" ' % (email, password))
            row = cursor.fetchone()
            self.current_user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        except pymysql.MySQLError as error:
            print('Failed to retrieve user from database. Error is {}'.format(error))

    def find_all_users(self):
        if self.users is not None:
            self.users.clear()
        try:
            self.get_user_by_id()
            self.update_average()
            connection = self.set_connection()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM users ORDER BY user_average DESC ')
            for row in cursor.fetchall():
                user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                self.users[user.name] = user
        except pymysql.MySQLError as err:
            print('failed to find all users. Error is {} '.format(err))

    def show_home_screen(self):
        self.home = Home(self)
        self.Frames['current'] = self.home
        self.home.pack(side="top")
        self.home.tkraise()

    def show_user_profile_screen(self):

        self.get_user_by_id()
        self.update_average()
        self.find_all_users()

        self.Frames['current'].destroy()
        user_view = UserProfile(self)
        self.Frames['current'] = user_view
        user_view.tkraise()

    def show_playground_screen(self):

        self.get_user_by_id()
        self.update_average()
        self.find_all_users()

        self.Frames['current'].destroy()
        playground = Playground(self)
        self.Frames['current'] = playground
        playground.tkraise()

