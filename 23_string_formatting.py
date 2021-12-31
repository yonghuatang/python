# string formatting (print) in Python
# 23 Jan 2021

x = 123.45678901

### There are different way to manipulate a string output

print(x)  # usual output

print(f"blablabla {:.2f}")  # f-string

print("%5.2f" % x)
# different notation, where 5 is the total characters including decimal point;
# 2 is the number of decimal places; 'f' denotes floating point number.

# %d ==> type int
# %s ==> type str



