print('''
Hello my friend
This is a small game by yonghua
Have fun!
You have to guess a number.
Rules: You must guess a number between 1~100
    If you see this " >>> "
    then you have no chance left :(

      ''')

x=int(input("Please enter a 1~100 number here 请输入一个1~100的数字: "))

while 0<=x<=87:
    print("Wrong.Please try again with a larger number.")
    x=int(input("Please enter a 1~100 number here 请输入一个1~100的数字: "))

while 89<=x<=100:
    print("Wrong.Please try again with a smaller number.")
    x=int(input("Please enter a 1~100 number here 请输入一个1~100的数字: "))

while x>=101:
    print("Wrong.Please try again with a number between 1 and 100.")
    x=int(input("Please enter a 1~100 number here 请输入一个1~100的数字: "))

while x<=-1:
    print("Wrong.Please try again with a number between 1 and 100.")
    x=int(input("Please enter a 1~100 number here 请输入一个1~100的数字: "))

if x==88:
    print("You have guessed the number!")
    print("If you want to learn how to programming, find yonghua")
    print("bye")
    print("Type \" quit() \" to exit and press \"OK\" to close the program")


    

    
