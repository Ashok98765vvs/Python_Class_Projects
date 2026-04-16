# public_access.py
class Student:
    def __init__(self, name, age):
        self.name = name      # Public
        self.age = age        # Public

s = Student("Ashok", 20)
print(s.name)   # ✅ Works anywhere
print(s.age)    # ✅ Works anywhere