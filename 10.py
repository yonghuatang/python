import ctypes
def mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%D %H:%M:%S")
mbox("WELCOME", "Have a nice day! You have one hour to play.", 0)
print("You began at the time", current_time)
a = str(current_time)[9:11]
b = str(current_time)[12:14]

x = int(input("""Enter your end time here
(example 3:46pm = 1546)
=======> """))
c = str(x)[0:2]
d = str(x)[2:4]
q = (int(c) - int(a))*60 + (int(d) - int(b))
while q > 60:
    mbox("ERROR", "Time's up", 0)
    
else:
    print("""


""")
    print("Good job!")
    print("You have played for ", q, "minutes.")





