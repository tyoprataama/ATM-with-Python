'''
Hi, I'm Tyo. College student from Economic background but really love computer science, because since I can run 'Hello World',
I can feel the power of my hand!!
Enjoy your code!
'''
from re import I
from atm_card import ATMCard
class Costumer:
    # Set up the very first pin from bank
    def __init__(self, id, prev_pin = 12345, prev_saldo = 10000):
        self.id = id
        self.prev_pin = prev_pin
        self.prev_saldo = prev_saldo
    # Set up the pin checker and saldo    
    def check_pin(self):
        return self.prev_pin
    def check_saldo(self):
        return self.prev_saldo
    def check_id(self):
        return self.id
    # Declare Method if costumer save or withdraw
    def debit_c(self, nominal):
        self.prev_saldo -= nominal
    def deposit_c(self, nominal):
        self.prev_saldo += nominal
        