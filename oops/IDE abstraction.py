from abc import ABC,abstractmethod

class Editor(ABC):
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def execute(Self):
        pass


class Vscode(Editor):
    def edit(self):
        print("vscode can edit")

    def debug(self):
        print("vscode can run debuge")
                              
    def execute(Self):
        print("vscode can execute")

obj=Vscode()
obj.edit()