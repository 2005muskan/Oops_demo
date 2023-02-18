# single inheritance
print("++++++++++++++++++++++++++++++")
class father:
    monay = 12000
    
    def show(self):
        print("make the most of life")
        
    @classmethod
    def showmonay(cls):
        print("its all gods gress")
        
class son(father):
    def display(self):
        print("thank you")

obj = son()
obj.display()

obj.show()
obj.showmonay()       

# multipal Inheritance

print("+++++++++++++++++++++++++++++++++++")

class father:
    def mobile1(self,name):
        print("hello")
        self.name=name
        print(self.name)
        
class mother:
    def mobile2(self,name):
        print("Hii")
        self.name=name
        print(self.name)
        
class son(father,mother):
    def num(self):
        print("byy")


obj=son()
obj.mobile1("muskan")
obj.mobile2("mahi")
obj.num()

#multilavel Inheritance
print("++++++++++++++++++++++++++++++++")
class father:
    def display(self,A,B):
        print("hello bhai")
        self.A = A
        self.B = B
        print(self.A)
        print(self.B)
class brother(father):
    def dis(self,X):
        print("good Afternoon")
        self.X = X
        print(self.X)
        
class sister(brother):
    def dek(self):
        print("please follow me")
        print(self.A)
        print(self.X)

obj=sister()
obj.display("samman","bhavi")

obj.dis("sir")

obj.dek()

print("++++++++++++++++++++++++++++++")

