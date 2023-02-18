class vari:

    def __init__(self):
        self.__x = "muskan"
        self._y = "Antim"

    def __cat__(self):
        print("Good Morning")

    def method1(self):
        print(self.__x)
        print(self._y)

class derrived(vari):

    def method2(self):
        print(self._y)

    def method3(self):
        print(self.__x)

obj = derrived()
obj.method2()
obj.mwthod1()
obj.method1()



