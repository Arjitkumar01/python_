class Stack:
    def __init__(self):
        self.stack = []  # Array

    # Push
    def push(self, item):
        self.stack.append(item)

    # Pop
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    # Peek
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    # Check Empty
    def is_empty(self):
        return len(self.stack) == 0

    # Size
    def size(self):
        return len(self.stack)

    # Display
    def display(self):
        print(self.stack)
        
        
n1=Stack()
n1.push(10)
n1.push(20)
n1.push(30)
n1.display()
n1.pop()
n1.display(20)

# using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "Stack Underflow"

        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def is_empty(self):
        return self.top is None

    def display(self):
        temp = self.top

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Peek:", stack.peek())

print("Pop:", stack.pop())

stack.display()