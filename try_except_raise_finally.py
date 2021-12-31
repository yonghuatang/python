# Created by YongHua 27/05/2020

# If you don't want to break the program caused by careless inputs,
# use the 'try' and 'except' block. Use 'raise' to manually cause
# an error and break the program when requirements are satisfied.
# The 'finally' block will always be executed and be the last to do so,
# which acts as a "cleaning move".


while True:
    try: 
        x = int(input("Please enter a number: "))
        
        if x < 0:
            print("This is a negative number.")
            
        if x == 0:
            print("This is zero.")
            
        elif x > 0:
            print("This is a positive number.")
        

    except:
        #raise("This is not a number! Try again.")
        #***This will intentionally cause an error and break the program.***
        print("This is not a number! Try again.")

    finally:   # 'finally' will always be executed and be the last to do so.
            print("I'm done.")

    

