#在Java中，所有类的最终父类都是Object
#在Python中，一个类没有直接的父类，它的父类也是Object
class Animal(object):
    #在Python中init方法相当于构造器
    #参数列表中，第一个位置是一个默认的参数叫作self，也就是实例本身，相当于Java的this
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def running(self):
        print("My Name is " + self.name + ", I'm running!!!")

#继承一个类时，将父类的类名放到Dog的括号中
class Dog(Animal):
    pass

class A(object):
    def running(self):
        print("AAAAA")

class Person(object):

    def printAnimal(self,animal):
        animal.running()

#主函数如此定义
if __name__ == '__main__':
    #创建实例
    #animal = Animal("WangCai",3,"male")
    #animal.running()
    #dog = Dog("Tom",3,"male")
    #dog.running()
    a = A()
    person = Person()
    person.printAnimal(a)