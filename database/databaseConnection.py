import pymysql

class SqlDbConnection(object):
    def __init__(self, default_user, default_password, database_name):
        self.default_user = default_user
        self.default_password = default_password
        self.database_name = database_name

    def get_connection(self):

        try:
            # create connexion
            connection = pymysql.Connect(user=self.default_user, passwd=self.default_password, autocommit=True)
            connection.commit()
            return connection
        except pymysql.MySQLError as error:
            print(error)
