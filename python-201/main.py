class Fraction():
    def __init__(self, whole: int = 0, fractional: int = 1) -> None:
        self.whole = whole
        self.fractional = fractional

    def reduce(self):
        numA, numB = self.whole, self.fractional

        if(numB > numA): numA, numB = numB, numA

        while(numB != 0):
            numA, numB = numB, numA % numB

        return Fraction(self.whole // numA, self.fractional // numA)
    
    def __str__(self) -> str:
        return f"({self.whole}/{self.fractional})"

def main():
    print(Fraction())
    print(Fraction(10))
    print(Fraction(2, 3))
    print(Fraction(12, 15).reduce())

if __name__ == "__main__": 
    main()