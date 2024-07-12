class Phone :

    name:str
    price:int
    model:str
    brand:str

    def __init__(self,name,price,model,brand):
        self.name=name
        self.price=price
        self.model=model
        self.brand=brand

    def display_phone(self):
        print(f"Phone name-{self.name}  phone price-{self.price}  Phone model-{self.model}  phone brand-{self.brand}")

    def __str__(self):
        return self.name

obj=Phone("PocoX2",18500,"new model","xioumi")
obj.display_phone()

print(obj)