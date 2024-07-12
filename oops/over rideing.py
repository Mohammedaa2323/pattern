class Parant:
    def car(self):
        print("zen")
    def bike(self):
        print("acesses")

class Child(Parant):
    def car(self):
        print("toyota supra")
    
ch=Child()
ch.car()
ch.bike()