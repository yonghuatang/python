# Created by Yonghua

# 'return'

def square_numbers(num):
    result = []
    for i in num:
        result.append(i**2)
    return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)

# or

my_nums2 = [x*x for x in [1,2,3,4,5]]

print(my_nums2)

# 'yield'

def square_numbers2(num):
    for i in num:
        yield i**2

my_nums3 = square_numbers2([1,2,3,4,5])

for j in my_nums3:
    print(j)

