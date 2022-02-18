'''
Hi, I'm Tyo. College student from Economic background but really love computer science, because since I can run 'Hello World',
I can feel the power of my hand!!
Enjoy your code!
'''
from mimetypes import init

class ATMCard:
    def __init__(self, default_pin, default_saldo):
        self.default_pin = default_pin
        self.default_saldo = default_saldo
    def cek_pin_awal(self):
        return self.default_pin
    def cek_saldo_awal(self):
        return self.default_saldo
        