class Person:
    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    @property 
    def Name(self):
        return self.__name
    
    # @Name.setter 
    def Name(self, value):
        self.__name == value
        
p = Person("Shubham",56,'M')

print(p.Name)
print(p.age)
print(p.gender)