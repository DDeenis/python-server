def hello() -> str:
    return "Hello"

def main() -> None:
    print(hello())

x = 10

def pair():
    return x, 2

def local_x():
    x = 20 # local variable
    return x

def change_x():
    global x
    x = 20;

print("x=%d, y=%d" % pair())