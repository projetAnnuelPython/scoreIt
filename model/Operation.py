from random import *


class Operation(object):
    def __init__(self):
        self.first_number = randint(0, 50)
        self.second_number = randint(0, 50)
        self.operator = choice(['+', '-', '*'])
        self.result = None

    def __str__(self):
        return '{} {} {}'.format(str(self.first_number), str(self.operator), str(self.second_number))

    def validate_operation(self):
        if self.operator == '*':
            self.result = self.first_number * self.second_number
            return str(self.first_number) + ' ' + str(self.operator) + ' ' + str(self.second_number)
        if self.operator == '-':
            if self.first_number >= self.second_number:
                self.result = self.first_number - self.second_number
                return str(self.first_number) + ' ' + str(self.operator) + ' ' + str(self.second_number)
            else:
                self.result = self.second_number - self.first_number
                return str(self.second_number) + ' ' + str(self.operator) + ' ' + str(self.first_number)
        if self.operator == '+':
            self.result = self.first_number + self.second_number
            return str(self.first_number) + ' ' + str(self.operator) + ' ' + str(self.second_number)
