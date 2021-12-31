# Created by YongHua 27/05/2020

# This is an example of 'try' 'except' 'raise' 'finally', as a candy vendor machine.

import time

number_of_candies = 10

while True:
	try:
		if number_of_candies == 0:
			break

		print("""
			Welcome
			How many candies do you want to buy?
			The price for one candy is $ 0.50.
        """)
		print("We have", number_of_candies, "candy/candies.")
		x = int(input())

		if x <= 0:
			print("ERROR.")
			continue

		if x > number_of_candies:
			print("Stock insufficient. Please purchase a smaller amount.")

		elif x <= number_of_candies:
			print("Added to cart successfully.")
			

	except:
		print("THIS IS NOT A VALID NUMBER. TRY AGAIN.")


	finally:

		if x <= 0:
			print("TRANSACTION VOID.")
			continue

		if 0 < x <= number_of_candies:
		    print("The total price is $", 0.5*x, ".")
		    number_of_candies = number_of_candies - x
		    print("TRANSACTION DONE.")	 
		    print("The amount of stock left in the machine is ", number_of_candies, "candy/candies.")
		    continue

		if x > number_of_candies:
			if number_of_candies == 0:
				break
			print("TRANSACTION FAILED. PLEASE TRY AGAIN.")	
			print("The amount of stock left in the machine is ", number_of_candies, "candy/candies.")		
			
time.sleep(3)

print("Out of stock.")

time.sleep(10)
