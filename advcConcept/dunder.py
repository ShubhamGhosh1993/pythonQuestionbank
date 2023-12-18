class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __del__(self)->None:
        print(f"Deconstruct the object {self}")
        
class Vector:
    def __init__(self, x, y) -> None:
        self.x=x
        self.y=y
        
    def __add__(self ,other):
        return Vector(self.x+other.x, self.y+other.y)
    
    def __repr__(self) -> str:
        return f"X: {self.x} Y: {self.y}"
        
p = Person("Shubham", 29)
v1 = Vector(5,6)
v2 = Vector(51,66)
v3 = v1+v2
print(v3)
print(p.name)
print(p.age)

'''
"Dunder" is a colloquial term for double underscores, and in Python, dunder methods refer to special methods that have double underscores at the 
beginning and end of their names. These methods are also known as magic methods or special methods, and they allow classes to define or customize behavior 
for various operations. Dunder methods are automatically called by the Python interpreter in response to certain language constructs or operations.

Here are some common dunder methods in Python:

1. **`__init__(self, ...)`:**
   - The constructor method. It is called when an object is created from a class and is used for initializing attributes.

2. **`__str__(self)`, `__repr__(self)`:**
   - The string representation methods. `__str__` is called by the `str()` built-in function, and `__repr__` is called by the `repr()` 
   built-in function and used for the string representation of the object.

3. **`__len__(self)`:**
   - Called by the `len()` built-in function and should return the length of the object.

4. **`__getitem__(self, key)`, `__setitem__(self, key, value)`, `__delitem__(self, key)`:**
   - Called for getting, setting, and deleting items using square bracket notation (`[]`) on the object.

5. **`__iter__(self)`, `__next__(self)`:**
   - Used to make an object iterable. `__iter__` returns an iterator object, and `__next__` is called to get the next item from the iterator.

6. **`__contains__(self, item)`:**
   - Called by the `in` operator to determine if an item is present in the object.

7. **`__call__(self, ...)`:**
   - Enables an instance of a class to be called as a function. This is achieved by defining the `__call__` method in the class.

8. **`__eq__(self, other)`, `__ne__(self, other)`, `__lt__(self, other)`, `__le__(self, other)`, `__gt__(self, other)`, `__ge__(self, other)`:**
   - Comparison methods. These are used to define the behavior of comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`) for instances of a class.

9. **`__add__(self, other)`, `__sub__(self, other)`, ... :**
   - Arithmetic methods. These are used to define the behavior of arithmetic operators (`+`, `-`, `*`, `/`, etc.) for instances of a class.

10. **`__enter__(self)`, `__exit__(self, exc_type, exc_value, traceback)`:**
    - Used for context management using the `with` statement. `__enter__` is called when entering the block, and `__exit__` is called when exiting the block.

These are just a few examples, and there are many more dunder methods that provide customization points for various Python language features. 
Understanding and using dunder methods can help you create classes that integrate seamlessly with Python's syntax and built-in functions.
'''