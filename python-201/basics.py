print('Hello')

x = "12"
#print(x + 1) # Error
print(int(x) + 1)
print(x + str(1))

x = 12
print(x + 1)
#print(x + str(1)) # Error

x = int(input("x = "))
if x < 10:
    print("< 10")
elif x < 20:
    print("10..19")
else:
    print(">= 20")