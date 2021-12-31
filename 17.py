print("""
Hi!
How are you today?
""")

from datetime import date
now = date.today()
print('The date today is', now, now.strftime("%A"))

for x in range(1, 101):
    if x%3 == 0:
        print("OH IT'S FACTOR OF 3!")
        pass
    
    else:
        print(x)

print("DONE")

        




