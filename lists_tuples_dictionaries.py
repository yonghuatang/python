# lists, tuples and dictionaries
# Created by YongHua


# lists are *mutable* objects
# enclosed in square brackets '[]'

a = ['apple', 'orange', 123]

# tuples are *immutable* objects
# enclosed in parenthesis '()'

b = ('Ali', 'Adam', 'Muthu')

# dictionaries are unordered collection of data: keys and values
# enclosed in curly brackets '{}'

c = {
	'firstname' : 'Mike',
	'lastname' : 'Henry',
	'age' : 24,
	'gender' : 'male',
	'work' : 'professor'
	'courses' : ['Math', 'Science']
}

print('This is a list. ', a)
print('This is a tuple. ', b)
print('This is a dictionary. ', c)
print(c.get('courses'))

# Iterate through dictionaries

for i,j in c.items():
	print(i, j)

for i in c.keys():
	print(i)

for j in c.values():
	print(j)

# to 'append' a dictionary, we use the following expression:
c["lorem"] = "ipsum"
# where "lorem" is the key, and "ipsum" is the corresponding value.