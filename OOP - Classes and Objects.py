# Object-Oriented Programming --- Classes and Objects
# Created by YongHua

class Customer:
	def __init__(self, First_Name, Last_Name, Age, Gender):
		self.first_name = First_Name
		self.last_name = Last_Name
		self.age = Age
		self.gender = Gender
		self.email = First_Name + '.' + Last_Name + '@xyzcompany.com'


person_1 = Customer('Adam', 'Phillips', 23, 'Male')
person_2 = Customer('John', 'Fromage', 17, 'Male')

# Another method for defining.
#
#person_1.first_name = 'Adam'
#person_1.last_name = 'Phillips'
#person_1.age = 23
#person_1.gender = 'Male'
#
#person_2.first_name = 'John'
#person_2.last_name = 'Fromage'
#person_2.age = 17
#person_2.gender = 'Male'

print(person_1.email)
print(person_2.email)

print("Done.")




