class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an element to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._items) == 0

    def __str__(self):
        return f"Stack({self._items})"

    def __len__(self):
        return len(self._items)



if __name__ == "__main__":
    stack = Stack()

    print("Initial stack:", stack)
    print("Is empty?", stack.is_empty())


    for x in [10, 20, 30]:
        stack.push(x)
        print(f"Pushed {x}: {stack}")

    print("\nPeek:", stack.peek())
    print("After peek:", stack)

    print("\nPop:", stack.pop())
    print("After pop:", stack)

    print("\nPop:", stack.pop())
    print("After pop:", stack)

    print("\nIs empty?", stack.is_empty())
    print("Final stack:", stack)