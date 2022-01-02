## args

def person(name, *data):
    print(f"Name: {name}")
    print(data)


person("Jason", 20, "London","0123456789")


## kwargs

def person(name, **data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i, '==>', j)


person("Jason", age=20, city="London", phone="0123456789")
