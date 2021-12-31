import time
moneyleft = 100

while True:
    while True:
        if moneyleft <= 0:
            print("Out of stock!")
            time.sleep(1.5)
            break
    
        x = float(input("How much money do you want? "))
    
        if x <= moneyleft and x > 0:
            print("Connecting to server...please wait.")
            time.sleep(3.5)
            print("Withdrawing", float(x), "dollars...please wait.")
            time.sleep(2.5)
            print("Transcation successful! Withdrawed", x, "dollars.")
            moneyleft = moneyleft - x

        elif x > moneyleft:
            print("Connecting to server...please wait.")
            time.sleep(2)
            print("Balance insufficient! You have", moneyleft, "dollars left." )
            time.sleep(0.5)

        elif x < 0:
            print("Please enter a valid amount.")
            print("Reconnecting...")
            time.sleep(1.25)

    y = float(input("Do you want to reload credit? Please enter the amount of cash: "))
    moneyleft = y
    time.sleep(1)
    print("Now you have", y, "dollars left!")

    

    
