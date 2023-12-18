def myDecorator(func):
    def wrapper(*args, **kargs):
        print("I am decorating the function")
        return func(*args, **kargs)
    return wrapper

@myDecorator
def helloWorld():
    print("Hello World!")

@myDecorator
def greeting(person):
    return f"Hello {person}"
    
helloWorld()
print(greeting("Shubham"))