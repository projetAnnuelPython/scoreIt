import tkinter as tk;
from tkinter import *
import datetime
from model.Operation import Operation

LARGE_FONT = ("Verdana", 18)

class Playground(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self, controller)
        self.grid(row=0, column=0, sticky="nsew")

        self.wrong_response_text = "Faux! La vraie réponse est "
        self.right_response_text = "Bravo! Bonne réponse"

        self.is_operation_launched = False

        self.controller = controller
        self.operation = None
        self.operation_text = StringVar()
        self.operation_text.set(' ')

        self.sentence_text = StringVar()
        self.sentence_text.set(' ')
        self.label_countdown = Label(self, textvariable=self.sentence_text)
        self.label_countdown.pack(pady=10)

        self.label_operation = Label(self, textvariable=self.operation_text, font=LARGE_FONT)
        self.label_operation.pack(anchor=W, padx=210, pady=5)

        self.label_equal = Label(self, text=' = ', font=LARGE_FONT)

        self.given_response = StringVar()
        self.response_entry = Entry(self, textvariable=self.given_response)

        self.submit_response = Button(self, text='SOUMETTRE', command=lambda: self.on_response_submitted())

        self.go_back_button = Button(self, text='MES STATISTIQUES', command=lambda: self.go_to_user_profile())
        self.go_back_button.pack(side=BOTTOM, pady=15)

        self.start_play_button = Button(self, text='NOUVELLE OPERATION',
                                        command=lambda: self.launch_operation())
        self.start_play_button.pack(side=BOTTOM, pady=5)

    def on_response_submitted(self):

        given_response = self.given_response.get()

        if int(given_response) == self.operation.result:
            self.sentence_text.set(self.right_response_text)
            self.controller.update_score(True)
        else:
            self.sentence_text.set(self.wrong_response_text + ' ' + str(self.operation.result))
            self.controller.update_score(False)

        self.response_entry.delete(0, 'end')
        self.controller.update_average()

    def launch_operation(self):

        self.controller.get_user_by_id()
        self.controller.update_total_questions()

        self.is_operation_launched = True

        self.operation = Operation()
        self.operation_text.set(self.operation.validate_operation())
        self.label_equal.pack(anchor=W, padx=230, pady=5)
        self.response_entry.pack(anchor=W, padx=200, pady=5)
        self.submit_response.pack(anchor=W, padx=200, pady=5)

    def update_countdown(self):
        start = datetime.datetime.now()
        start_seconds = start.second
        end_seconds = start.second + 5
        counter = 5
        while start_seconds <= end_seconds:
            now = datetime.datetime.now()
            now_seconds = now.second
            if now_seconds == (start_seconds + 1):
                self.sentence_text.set(self.update_countdown_label(counter))
                start_seconds = now_seconds
                counter = counter - 1

    def update_countdown_label(self, countdown_value):
        splited_text = self.sentence_text.get().split(' ')
        splited_text.insert(3, str(countdown_value))
        result = ''
        for string in splited_text:
            result = result + string + ' '
        return result


        # def my_count_down(self):
        #     counter = 1000000
        #     while counter >= 0:
        #         self.update_countdown_label(counter)
        #         counter = counter - 200000

    def go_to_user_profile(self):
        self.controller.find_all_users()
        self.controller.show_user_profile_screen()
