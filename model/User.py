class User(object):
    def __init__(self, user_id, name, email, password, score, total_questions):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.score = score
        self.total_questions = total_questions
