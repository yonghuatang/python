def count_e(str):
    c = 0
    for letter in str:
        if letter == 'e':
            c += 1
    return c


print(count_e("abcde"))

def count_an(str):
    c = 0
    for i in range(len(str)):
        if str[i] == 'a' and str[i+1] == 'n':
            c += 1
    return c


print(count_an("anantanan"))

def swap_case(str):
    result = ''
    for c in range(len(str)):
        if str[c].isupper():
            result += str[c].lower()
        else:
            result += str[c].upper()
    return result


print(swap_case("AbCdEfGhIjKlM"))

def product_list(a, b):   # assume that list a and b have the same length
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


print(product_list([1,2,3], [4,5,6]))

def overlap(a, b):
    ans = []
    for i in a:
        for j in b:
            if i == j and i not in ans:
                ans.append(i)
    return ans


print(overlap([1,2,3,4], [4,19,410,2]))







