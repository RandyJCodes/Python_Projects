# encapsulation project
# Python 3.9.5
# Author: Randall Jackson
#
#
# Purpose: Using parent and child classes to abstract data
# 
#
from abc import ABC, abstractmethod

#Parent Class
class Ring(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
    # this funciton is telling us to pass in an arg, but we won't tell you how or what
    # kind of data it will be.
        @abstractmethod
        def payment(self, amount):
            pass

#Child class
class DebitCardPayment(Ring):
#here we've defined how to implement the payment function from its parent pySlip class.
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $1000 limit for the ring purchase.".format(amount))

obj = DebitCardPayment()
obj.paySlip("$1500")
obj.payment("$1500")
