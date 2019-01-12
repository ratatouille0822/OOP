class gun:
    def __init__(self,model,bullets = 20):
        self.model = model
        self.bullets = bullets
    def __str__(self):
        return "这是一把 %s，现在有 %d发子弹" % (self.model,self.bullets)
    def shoot(self):
        self.bullets -= 1
        print("发射了1发子弹，还剩%d发"%self.bullets)
    def load(self):
        self.bullets += 1
        print("上了一发子弹，现在还有%d发"%self.bullets)

class soldier:
    def __init__(self,name,gun = None):
        self.name = name
        self.gun = gun
    def __str__(self):
        if self.gun is not None:
            return "士兵%s 有一把%s枪" % (self.name,self.gun.model)
        else:
            return "士兵%s 没有枪" % self.name
    def fire(self):
        if self.gun is not None and self.gun.bullets is not 0:
            self.gun.shoot()
        elif self.gun is None:
            print("%s没有枪，不能射击"% self.name)
        elif self.gun.bullets is 0:
            print("没有子弹了，不能射击")
        else:
            print("一定发生了什么怪事")

    def load(self):
        self.gun.load()


AK47 = gun("AK47",20)
print(AK47)
xusanduo = soldier("许三多",AK47)
print(xusanduo)
xusanduo.fire()
xusanduo.load()
for i in range(1,25):
    xusanduo.fire()

captain = soldier("队长")
print(captain)
captain.fire()




