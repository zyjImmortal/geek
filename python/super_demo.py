class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()



class Animal:

    def __init__(self, name):
        self.name = name


class Bird(Animal):

    def __init__(self, age):
        self.age = age
        print(self.name)

# bird = Bird(12)

import logging
class LoggingDict(dict):

    def __setitem__(self, key, value):
        logging.info("setting {} to {}".format(key, value))
        super(LoggingDict, self).__setitem__(key, value)