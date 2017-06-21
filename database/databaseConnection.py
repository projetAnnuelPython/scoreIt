import pymysql
import database.Tables as Tables


class SqlDbConnection(object):
    def __init__(self, settings):
        self.default_user = settings['sql']['login']
        self.default_password = settings['sql']['password']
        self.database_name = settings['sql']['database_name']

    def get_connection(self):
        try:
            # create connexion
            connection = pymysql.Connect(user=self.default_user, passwd=self.default_password, autocommit=True)
            connection.select_db(self.database_name)
            connection.commit()
            return connection
        except pymysql.MySQLError as error:
            print("Enable to create database. Error is {}".format(error))

    def fixtures_create_db(self):
        try:

            connection = self.get_connection()
            cursor = connection.cursor()

            # drop database
            create_db_req = "DROP DATABASE IF EXISTS {0}".format(self.database_name)
            cursor.execute(create_db_req)

            # create database
            create_db_req = "CREATE DATABASE IF NOT EXISTS {0}".format(self.database_name)
            cursor.execute(create_db_req)

        except pymysql.MySQLError as error:
            print(error)

    def create_tables(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        table_entity = Tables.Tables()
        table_list = table_entity.TABLES

        try:
            for name, ddl in table_list.items():
                cursor.execute(ddl)
                connection.commit()
                print("{} table successfully created".format(name))
        except pymysql.MySQLError as error:
            print("failed to create table.Error is {}".format(error))

    def fixtures_insert_users(self, users):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            for user in users:
                cursor.execute('INSERT INTO users(user_name, email, password, score, total_questions, user_last_name, user_average)'
                               'VALUES("%s","%s","%s","%s","%s","%s","%s")' % (user['user_name'], user['email'],  user['password'], user['score'], user['total_questions'], user['user_last_name'], user['user_average']))
                connection.commit()
                print("user {} successfully saved".format(user['user_name']))
        except pymysql.MySQLError as error:
            print("Fail to save default users in database".format(error))

