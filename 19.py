def func():
    for i in range(1,6):
        yield i

x = func()
print(x)   # prints generator object

for j in x:
    print(j)