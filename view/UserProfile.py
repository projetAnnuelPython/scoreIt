import tkinter as tk;
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class UserProfile(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller

        label_firstname = Label(self, text="{} {}".format(self.controller.current_user.name, self.controller.current_user.user_last_name))
        label_firstname.pack(side=TOP, pady=30)

        label_stats = Label(self, text='Statistiques \t\t\t Classement')
        label_stats.pack(side=TOP)

        name = ['gagnés', 'perdus']
        data = [self.controller.current_user.score,
                ((self.controller.current_user.total_questions * 10) - self.controller.current_user.score)]
        colors = ['green', 'red']
        explode = (0, 0)
        fig = plt.figure(figsize=(2, 2))
        patches, texts, auto_texts = plt.pie(data, radius=0.4, explode=explode, labels=name, colors=colors,
                                             autopct='%1.1f%%', startangle=50, shadow=True)
        texts[0].set_fontsize(7)
        texts[1].set_fontsize(7)
        plt.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack(anchor=W, side=LEFT, padx=10)
        canvas.draw()

        list_box = Listbox(self, borderwidth=0)
        index = 1
        for user in self.controller.users:
            current_user = self.controller.users[user]
            print('list box user {} average {}'.format(current_user.name, current_user.user_average))
            list_box.insert(index, "{}.   {}  {}/{}".format(index, current_user.name, current_user.score,
                                                            (current_user.total_questions * 10)))
            index = index + 1
        list_box.pack_propagate(True)
        list_box.pack(side=RIGHT, expand=1, anchor=E, padx=20, pady=80)
        go_play = tk.Button(self, text='JOUER', command=lambda: self.controller.show_playground_screen())
        go_play.pack(side=BOTTOM)





