from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def start(this):
        pass
    @abstractmethod
    def acc(this):
        pass
    @abstractmethod
    def stop(this):
        pass

class Shift(Car):

    def start(this):
        print("shift start")

    def acc(this):
        print("shift acc")

    def stop(this):
        print("shift stop")
    
ch=Shift()

ch.start()
ch.acc()