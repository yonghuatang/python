# Python Decorators

def my_decorator(func):
    def wrapper():  # use a 'wrapper' function
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator  # decorator
def say_whee():
    print("Whee!")


say_whee()  # call the function after modified by a decorator


### another example below

def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@do_twice
def greet():
    print("Hi!")


greet()

@do_twice
def greet(name):
    print(f"Hi! {name}")  # doesn't work
    # must change inner wrapper function to wrapper(*args, **kwargs) to accept arbitrary number of arguments


greet("Tang")
