class Tables(object):
    def __init__(self):
        self.TABLES = {
            'users': "CREATE TABLE `users`(user_id INT NOT NULL AUTO_INCREMENT,"
                     "PRIMARY KEY (user_id), user_name VARCHAR(255), email VARCHAR(255), password VARCHAR(255),"
                     "score INT, total_questions INT)"
        }

