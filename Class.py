class Students:
    def __init__(self, name, student_id):
        self.name = name
        self._student_id = student_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if isinstance(value, int) and value > 0:
            self._student_id = value
        else:
            raise ValueError

    def status(self):
        return f"Name: {self.name}, Student ID: {self.student_id}"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_linked_list(head):
    current = head
    while current:
        print(current.data.status(), end=" -> ")
        current = current.next
    print("None")


def insert_student(head, previous_student_id, new_student):
    current = head
    while current:
        if current.data.student_id == previous_student_id:
            new_node = Node(new_student)
            new_node.next = current.next
            current.next = new_node
            return head
        current = current.next
    print("Student not present")
    return head


def delete_student(head, student_to_delete):
    current = head
    prev = None

    if current and current.data.student_id == student_to_delete:
        return current.next

    while current:
        if current.data.student_id == student_to_delete:
            prev.next = current.next
            return head
        prev = current
        current = current.next

    print("Student not present")
    return head


s1 = Students("ASHOK", 4533352)
s2 = Students("CHARAN", 4533353)
s3 = Students("SRIMAN", 4533354)

head = Node(s1)
head.next = Node(s2)
head.next.next = Node(s3)

traverse_linked_list(head)

head = insert_student(head, 4533353, Students("BOB BROWN", 4533355))
traverse_linked_list(head)

head = delete_student(head, 4533352)
traverse_linked_list(head)