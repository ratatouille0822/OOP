class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return "%s的体重是%.2f公斤" %(self.name,self.weight)
    def eat(self):
        self.weight += 1.0
        print("%s 吃了东西,体重变为%.2f公斤"%(self.name,self.weight))
    def jog(self):
        self.weight -= 0.5
        print("%s 跑了步，体重变为%.2f公斤"%(self.name,self.weight))


xiaoming = Person("小明",75.0)
xiaoming.eat()
xiaoming.eat()
xiaoming.jog()
print(xiaoming)

xiaomei = Person("小美",45.0)
xiaomei.eat()
xiaomei.jog()
print(xiaoming)
print(xiaomei)
