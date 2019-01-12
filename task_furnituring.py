class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "这是%s，占地%.2f平方米" % (self.name,self.area)

class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return "这是一个%.2f的%s\n目前还有%.2f m2 剩余空间\n现在屋内摆放了%s\n"\
               % (self.area,self.house_type,self.free_area,",".join(self.item_list))
    def add_item(self,HouseItem):
        if self.free_area >= HouseItem.area:
            self.free_area -= HouseItem.area
            self.item_list.append(HouseItem.name)
            print("添加了一个%s,现在屋子内还剩%.2f m2" %(HouseItem.name,self.free_area))
        else:
            print("没有足够空间来添加%s"%HouseItem.name)
bed1 = HouseItem("bed1",4.0)
chest1 = HouseItem("chest1",2.0)
table1 = HouseItem("table1",1.5)
monster = HouseItem("monster",100.0)

house1 = House("公寓",100.0)
print(house1)
house1.add_item(bed1)
print(house1)

house1.add_item(chest1)
print(house1)
house1.add_item(table1)
print(house1)
house1.add_item(monster)
print(house1)
