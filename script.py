class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def status(self):
        avg = self.average()
        return f"{self.name}: scores={self.scores}, avg={avg}"


student = Student("Ashok Shakarappa")

while True:
    user_input = input("Enter a score (or 'q' to quit): ").strip().lower()
    if user_input == 'q':
        break
    try:
        score = float(user_input)
        student.add_score(score)
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

print(student.status())