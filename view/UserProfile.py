from model.User import User
import tkinter as tk;
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class UserProfile(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.controller = controller

        top_pane = PanedWindow()
        label_firstname = Label(top_pane, text=self.controller.current_user.name)
        top_pane.add(label_firstname)
        label_lastname = Label(top_pane, text=self.controller.current_user.user_last_name)
        top_pane.add(label_lastname)
        top_pane.grid(row=0, column=0, rowspan=2, pady=10)

        mid_pane = PanedWindow()
        label_stats = Label(mid_pane, text='Statistiques')
        mid_pane.add(label_stats)
        mid_pane.grid(row=2, column=0, padx=50)

        mid_pane_right = PanedWindow()
        label_ranking = Label(mid_pane_right, text='Classement')
        mid_pane_right.add(label_ranking)
        mid_pane_right.grid(row=2, column=30, padx=170)


        name = ['gagnés', 'perdus']
        data = [self.controller.current_user.score, ((self.controller.current_user.total_questions * 10) - self.controller.current_user.score)]
        colors = ['green', 'red']
        explode = (0, 0)
        fig = plt.figure(figsize=(2, 2))
        patches, texts, auto_texts = plt.pie(data, radius=0.4, explode=explode, labels=name, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
        texts[0].set_fontsize(6)
        texts[1].set_fontsize(6)
        plt.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self.controller)
        canvas.get_tk_widget().grid(row=0, column=0, sticky='nw', pady=75)
        canvas.draw()


        list_box = Listbox(self.controller, borderwidth=0)
        index = 1
        for user in self.controller.users:
            current_user = self.controller.users[user]
            list_box.insert(index, "{}.   {}  {}/{}".format(index, current_user.name, current_user.score, (current_user.total_questions*10)))
            index = index + 1
        list_box.grid(row=0, column=0, sticky='nse', pady=100)

        go_play = Button(self, text="JOUER", command=lambda: self.controller.go_play())
        go_play.grid(row=0, column=0)

