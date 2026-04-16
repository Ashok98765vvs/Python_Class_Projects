# protected_access.py
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks    # Protected

class TopStudent(Student):
    def show(self):
        # ✅ Accessible in subclass
        print(f"{self.name} scored {self._marks}")

s = TopStudent("Ashok", 95)
s.show()

# Can still access outside but NOT recommended
print(s._marks)   # ⚠️ Works but bad practice