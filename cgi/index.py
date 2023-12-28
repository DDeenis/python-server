#!D:/Python3/python.exe

print("Content-Type: text/html")
print("")
with open('static/home.html', mode='r') as f:
    print(f.read())