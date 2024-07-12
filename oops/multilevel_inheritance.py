# multievel inheritance


class Parant1:
    def m1(self):
        print("inside parant1 m1 method")

class Parant2(Parant1):
    def m2(self):
        print("inside parant2 m2 method")

class Child(Parant2):
    def c(self):
        print("inside child c method")

ch=Child()
ch.c()
ch.m2()
ch.m1()