from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        """Interface Method"""
        
# p1=IPerson()
# print(p1.person_method());

class Student(IPerson):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Student Name"
        
    def person_method(self):
        print(f"I am a {self.name}")
        
class Teacher(IPerson):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Teacher Name"
        
    def person_method(self):
        print(f"I am a {self.name}")
        
s1=Student()
t1=Teacher()

# t1.person_method()
# s1.person_method()

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Teacher":
            return Teacher()
        if person_type == "Student":
            return Student()
        
bp1=PersonFactory()
person = bp1.build_person("Student")

person.person_method()