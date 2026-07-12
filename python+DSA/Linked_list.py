# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# Each node has:
# data → stores the value.
# next → points to the next node.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create nodes
# first = Node(10)
# second = Node(20)
# third = Node(30)

# # Connect nodes
# first.next = second
# second.next = third

# # Traverse the linked list
# current = first

# while current:
#     print(current.data)
#     current = current.next

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

first=node("Arjit")
second=node("Abhi")
third=node("Anything")


first.next=second
second.next=third

head = first
current = head

while current:
    print(current.data)
    current=current.next


#  ADDING A NEW NODE AT THE STARTING OF THE LINKED LIST:

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
    
# first=node(101)
# second=node(202)
# third=node(303)
# four=node(404)

# first.next=second
# second.next=third
# third.next=four

# new_node=node(505)
# new_node.next=first
# first=new_node

# current=first

# while current:
#     print(current.data)
#     current=current.next

# =============================================================INSERTING AT THE ENDING

# class Node:
#     def __init__(self,data):
#         self.data =data
#         self.next=None
        
# n1=Node("first")
# n2=Node("second")
# n3=Node("third")

# n1.next=n2
# n2.next=n3


# new_node=Node ("forth")

# current=n1

# while current.next:
#     current=current.next
    
# current.next = new_node
    

# current= n1

# while current:
#     print(current.data)
#     current=current.next


# ====================================================DOUBLE LINKED LIST


# class Node:
#     def __init__(self, data):
#         self.prev = None
#         self.data = data
#         self.next = None


# # Create nodes
# first = Node(10)
# second = Node(20)
# third = Node(30)

# # Connect nodes
# first.next = second
# second.prev = first

# second.next = third
# third.prev = second

# # Traverse Forward
# print("Forward Traversal")

# current = first

# while current:
#     print(current.data)
#     current = current.next


# # Traverse Backward
# print("Backward Traversal")

# current = third

# while current:
#     print(current.data)
#     current = current.prev
    
    
# # ========================================================CIRCULAR LINKED LIST


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create nodes
# first = Node(10)
# second = Node(20)
# third = Node(30)

# # Connect nodes
# first.next = second
# second.next = third
# third.next = first      # Circular connection

# # Traverse Circular Linked List
# current = first

# while True:
#     print(current.data)
#     current = current.next

#     if current == first:
#         break