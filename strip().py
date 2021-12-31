# strip() method

# The strip() method returns a copy of the string in which all chars
# have been stripped from the beginning and the end of the string
# (default whitespace characters).

x = str(input("Please enter a string: "))

print(x.strip())

mylist = x.split(sep=' ')

for i in mylist:
    print(i)