class Menu:
    name:str
    def __init__(self,name):
        self.name=name


    def __str__(self):
        return self.name
    
class Dish(Menu):
    ingrediance:str
    price:int
    def __init__(self, name,ingrediance,price):
        super().__init__(name)
        self.ingrediance=ingrediance
        self.price=price
        print(self.name,self.ingrediance,self.price)
item=Dish("pinapple juice","pinapple","30")
