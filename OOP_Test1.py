class Cat:
    def __init__(self,name,food):
        self.name = name
        self.food = food
    def eat(self):
        print("%s eats %s" % (self.name,self.food))
    def drink(self):
        print("%s drinks" % self.name)

Tom = Cat("Tom","Fish")
Tom.eat()
Tom.drink()
Tod = Cat("Tod","Salmon")
Tod.eat()
Tod.drink()
