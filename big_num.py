# Find the largest integer.

big_num = 0

while True:
    n = int(input("Please enter a number (type 0 to exit): "))
    if n == 0:
        print("Program terminated. . .")
        break
    if n > big_num:
        big_num = n
        print(big_num)
