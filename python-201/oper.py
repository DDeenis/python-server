x = 14
y = 6

res = "x + y = %d" % (x + y);
res = "%d + %d = %d" % (x, y, x + y)
print(res)
print("%d - %d = %d" % (x, y, x - y))
print("%d * %d = %d" % (x, y, x * y))
print("%d / %d = %f" % (x, y, x / y))
print("%d // %d = %d" % (x, y, x // y))
print("%d ** %d = %d" % (x, y, x ** y))
print("%d %% %d = %d" % (x, y, x % y))

print("range(10):", end=" ")
for i in range(10):
    print(i, end=" ")
print()

x = 10
y = 20 if x < 10 else 5

while x > 0:
    print(x, end=" ")
    x -= 1
else:
    print()