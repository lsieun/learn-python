class Animal(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def running(self):
        print("My Name is " + self.name + ", I'm running!!!")

if __name__ == '__main__':
    animal = Animal("TomCat", 3, "male")

    #getattr
    noneExistAttr = getattr(animal, "noneExistAttr", "defaultValue")
    print("noneExistAttr: " + noneExistAttr)

    #hasattr + getattr
    if(hasattr(animal,"name")):
        nameAttr = getattr(animal,"name","WangCai")
        print("Animal Name is: " + nameAttr)

    #setattr + getattr
    setattr(animal, "name", "JerryMouse")
    nameAttr = getattr(animal, "name", "WangCai")
    print("Animal's New Name is: " + nameAttr)


