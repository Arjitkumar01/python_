class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue
    def enqueue(self, item):
        self.queue.append(item)

    # Dequeue
    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        return self.queue.pop(0)

    # Front
    def front(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue[0]

    # Rear
    def rear(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue[-1]

    # Empty
    def is_empty(self):
        return len(self.queue) == 0

    # Size
    def size(self):
        return len(self.queue)

    # Display
    def display(self):
        print(self.queue)
        
        
# using linked list 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue Underflow"

        removed = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed

    def peek(self):
        if self.front:
            return self.front.data
        return None

    def is_empty(self):
        return self.front is None

    def display(self):
        temp = self.front

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Peek:", q.peek())

print("Dequeue:", q.dequeue())

q.display()