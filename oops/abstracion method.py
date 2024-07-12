from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelarate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Swift(Car):
    def start(self):
        print("swift starting")

    def accelarate(self):
        print("swift accelarate")

    def stop(self):
        print("swift stop")

obj=Swift()
obj.start()
obj.accelarate()
obj.stop()





class Car(ABC):
    @abstractmethod
    def __init__(self,name,brand,model):
        pass
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelarate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Swift(Car):
    def __init__(self, name, brand, model):
        self.name=name
        self.brand=brand
        self.model=model    
    def start(self):
        print("swift starting")

    def accelarate(self):
        print("swift accelarate")

    def stop(self):
        print("swift stop")

obj=Swift("swift","suzuki","2020")
obj.start()
obj.accelarate()
obj.stop()
