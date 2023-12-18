def myDecorator():
    def wrapper():
        print("I am decorating the function")
        
    return wrapper

def helloWorld():
    print("Hello World!")