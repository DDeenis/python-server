class MyClass():
    x = 10

def demo1():
    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1.x, obj2.x, MyClass.x)
    MyClass.x = 20
    print(obj1.x, obj2.x, MyClass.x)
    obj1.x = 15
    print(obj1.x, obj2.x, MyClass.x)

class TheClass():
    x = 10
    def  __init__(self, a = 1, b = 2):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"({self.a}, {self.b})"
    
    def magnitude(self) -> int:
        return self.a + self.b

def demo2():
    obj1 = TheClass()
    print(obj1)
    print(TheClass(20, 30))
    print(TheClass(20))
    print(TheClass(b=30))
    print(obj1.magnitude())

def main():
    demo2()

if __name__ == "__main__":
    main()