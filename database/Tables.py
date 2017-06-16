class Tables(object):
    def __init__(self):
        self.TABLES = {
            'users': "CREATE TABLE `users`(user_id INT NOT NULL AUTO_INCREMENT,"
                     "PRIMARY KEY (user_id), name VARCHAR(255), email VARCHAR(255), passwordVARCHAR(255))"
        }
