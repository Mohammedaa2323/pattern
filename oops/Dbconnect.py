from abc import ABC,abstractmethod

class Dbconnect(ABC):
    @abstractmethod
    def __init__(self,user,password,port,database,attributes):
        pass
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def execute_query(self):
        pass
    @abstractmethod
    def close(self):
        pass

class Mydbconnect(Dbconnect):
    def __init__(self, user, password, port, database, attributes):
        self.user=user
        self.password=password
        self.port=port
        self.database=database
        self.attributes=attributes

    def connect(self):
        print("connected to dbconnect")

    def execute_query(self):
        print("execute the items")
    def close(self):
        print("close the items")

obj=Mydbconnect("mohammed","mohammedaa","123","DASTE","duheuid")
obj.connect()