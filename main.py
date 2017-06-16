from tool.JsonParser import JsonParser
from database.databaseConnection import SqlDbConnection

# load json resources
json_parser = JsonParser()
settings = json_parser.parsefile('settings')

sqlConnect = SqlDbConnection(settings['sql']['login'], settings['sql']['password'],
                             settings['sql']['database_name'])

sqlConnect.get_connection()
