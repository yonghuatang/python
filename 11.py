for i in range(2, 21):
	for j in range(2, i):
		if i % j == 0:
			print(f"{i} = {j} times {i // j}")
			break
				    
	else:
		print(i, " is a prime number!")

print("Done")
