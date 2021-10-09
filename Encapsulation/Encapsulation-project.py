# encapsulation project
# Python 3.9.5
# Author: Randall Jackson
#
#
# Purpose: Using a private methods to restrict access to
# functions and variable to be changed by mistake
#
class Protected:
    def __init__(self):
        self.__privateVar = 21

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
# Setting the private Var to another number
obj.setPrivate(300)
obj.getPrivate()
