import ctypes

my_int32 = ctypes.c_int32(1234)
# print(hex(my_int32.value))

class Metabolism():

    FATS_SHIFT = 0
    PROTEINS_SHIFT = 8
    CARBON_SHIFT = 16
    ACIDS_SHIFT = 24

    FATS_MASK = 0x000000FF
    PROTEINS_MASK = 0X0000FF00
    CARBON_MASK = 0x00FF0000
    ACIDS_MASK = 0xFF000000

    
    def __init__(self):
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    @property
    def fats(self):
        return self.balance & Metabolism.FATS_MASK

    @fats.setter
    def fats(self, value):
        elem = value << Metabolism.FATS_SHIFT
        self.balance += elem

    @property
    def proteins(self):
        return self.balance & Metabolism.PROTEINS_MASK
        

    @proteins.setter
    def proteins(self, value):
        elem = value << Metabolism.PROTEINS_SHIFT
        self.balance += elem

    @property
    def carbons(self):
        return self.balance & Metabolism.CARBON_MASK
    
    @carbons.setter
    def carbons(self, value):
        elem = value << Metabolism.CARBON_SHIFT
        self.balance += elem 
    
    @property
    def acids(self):
        return self.balance & Metabolism.ACIDS_MASK
    
    @acids.setter
    def acids(self, value):
        elem = value << Metabolism.ACIDS_SHIFT
        self.balance += elem 

    def printBalance(self):
        print(hex(self.balance))

        
m = Metabolism()
m.fats = 15
m.proteins = 255
m.carbons = 34
m.acids = 158
m.printBalance()
# print(m.fats)
