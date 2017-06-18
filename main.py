from tool.JsonParser import JsonParser
from database.databaseConnection import SqlDbConnection
from view.App import *
import tkinter as tk
import tkinter
#   self.root.bind('<FocusIn>', self.focus_in)
# load json resources
json_parser = JsonParser()
settings = json_parser.parsefile('settings')

sqlConnect = SqlDbConnection(settings['sql']['login'], settings['sql']['password'],
                             settings['sql']['database_name'])
sqlConnect.get_connection()
sqlConnect.fixtures_create_db()
sqlConnect.create_tables()
sqlConnect.fixtures_insert_users(settings['users'])

root = tk.Tk()
root.geometry('500x300+300+40')
root.title('SCORE IT')
root.resizable(width=False, height=False)


app = App(root)
app.pack(side="top", fill="both", expand=True)
root.mainloop()

