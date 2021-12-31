## args

def person(name, *data):
    print(name)
    print(data)

person('YongHua', 20, 'Kuala Lumpur', '0123456789')

## kwargs

def person(name, **data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i, '==>', j)

person('YongHua', age=20, city='Kuala Lumpur', phone='0123456789')
