class Book:

    name:str
    author:str
    pages:int
    price:int

    def __init__(self,name,author,pages,price):
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price

    def display_book(self):
        print(self.name,self.author,self.price,self.pages)

    def __str__(self):
        return self.name
        
obj=Book("adujivitham","baniyamin",200,350)
obj.display_book()
print(obj)