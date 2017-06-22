from tool.JsonParser import JsonParser
from database.databaseConnection import SqlDbConnection
from view.App import *
from view.Root import *

json_parser = JsonParser()
settings = json_parser.parsefile('settings')

sqlConnect = SqlDbConnection(settings)
sqlConnect.get_connection()
sqlConnect.fixtures_create_db()
sqlConnect.create_tables()
sqlConnect.fixtures_insert_users(settings['users'])


root = Root()

app = App(root)
app.set_db_connection_credentials(settings)

app.pack(side="top", fill="both", expand=True)

root.mainloop()

