from abc import ABC, abstractmethod


class IDE(ABC):

    @abstractmethod
    def editor(self):
        pass

    @abstractmethod
    def project_structure_window(self):
        pass

    @abstractmethod
    def execution_window(self):
        pass

    def syntax_checking(self):
        pass


class PyCharm(IDE):

    def editor(self):
        print("My editor is at right")

    def project_structure_window(self):
        print("my project structure window is at left")

    def execution_window(self):
        print("my execution windows pops up below editor when code is executed")

    def themes(self):
        print("i have more than 10 themes")


class Eclipse(IDE):

    def editor(self):
        print("my editor is at left")

    def project_structure_window(self):
        print("my project structure window is at right")

    def execution_window(self):
        print("my execution windows pops up above editor when code is executed")


pc = PyCharm()
ec = Eclipse()

pc.editor()
ec.editor()
pc.project_structure_window()
ec.project_structure_window()
pc.execution_window()
ec.execution_window()






