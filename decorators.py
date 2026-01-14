def decorator(func):
    def wrapper():
        print("i am about to execute a function...")
        func()
        print("i have executed this function....")
    return wrapper


def say_hello():
    print("Hello")

f = decorator(say_hello)
f()