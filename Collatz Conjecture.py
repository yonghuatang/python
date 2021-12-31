print('''
This a computer iteration for Collatz Conjecture.
PYTHON
yonghua
''')

x = int(input("Please enter a positive integer: "))

while x > 1:
    if (x % 2):
        x = 3*x + 1
    else:
        x = x // 2
    print(x, bin(x)[2: ], len(bin(x)) - 2)
    
    
        
