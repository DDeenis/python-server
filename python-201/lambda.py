def oper(lam) -> int:
    return lam(1, 2)

def main():
    lam1 = lambda x: print(x)
    lam1('test')
    lam2 = lambda x, y: print(x, y)
    lam2("Hello", "World")
    lam3 = lambda: print("No args")
    lam3()
    print(oper(lambda x, y: x + y))
    print(oper(lambda x, y: x - y))

if __name__ == "__main__":
    main()