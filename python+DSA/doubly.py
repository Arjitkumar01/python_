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


# class Node: 
#     def __init__(self, data):
#         self.data = data #this is to initialize the data of the node
#         self.next = None #this is to initialize the next pointer of the node to None
#         self.prev = None #this is to initialize the prev pointer of the node to None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None #this is to initialize the head pointer to None

#     def append(self, data):
#         new_node = Node(data) #this is to create a new node with the given data

#         if self.head is None:
#             self.head = new_node #this is to set the head pointer to the new node if the list is empty
#             return
        
#         last_node = self.head #this is to set the last_node pointer to the head of the list
#         while last_node.next:
#             last_node = last_node.next #this is to traverse the list until the last node is reached
#         last_node.next = new_node #this is to set the next pointer of the last node
#         new_node.prev = last_node #this is to set the prev pointer of the new node to the last node

#     def traverse_forward(self):
#         print("Forward traversal:")
#         current = self.head #this is to set the current pointer to the head of the list
#         while current:
#             print(current.data, end=" -> ") #this is to print the data of the current node
#             current = current.next #this is to set the current pointer to the next node in the list
#         print("None") #this is to print None at the end of the list

#     def traverse_backward(self):
#         print("Backward traversal:")
#         if self.head is None:
#             print("List is empty")
#             return

#         current = self.head
#         while current.next:
#             current = current.next

#         while current:
#             print(current.data, end=" -> ")
#             current = current.prev
#         print("None")

# print("Doubly Linked List:")
# dll = DoublyLinkedList()
# dll.append(1)
# dll.append(2)
# dll.append(3)
# dll.traverse_forward()
# dll.traverse_backward()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class DoublyLinkedlist:
    def __init__(self):
        self.head=None
        
    def add_at_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        
    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head= new_node
            return
        current=self.head
        while current.next:
            current=current.next
            
        current.next=new_node
        new_node.prev=current
        
    def add_at_position(self,data,key):
        new_node=Node(data)
        
        if self.head is None:
            print("key not found")
            return
        
        current=self.head
        
        while current is not None and current.data!=key:
            current=current.next
            
        if current is None:
            print("key not found")
            return
            
        if current.next is None:
            self.add_at_end(data)
            return
            

        new_node.next=current.next
        new_node.prev=current
        new_node.next.prev=new_node
        current.next=new_node
        
    
    
    def remove_at_begin(self):
        
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head=None
            return
            
        
        self.head=self.head.next
        self.head.prev=None
        
    def remove_at_end(self):
        
        if self.head is None:
            print("list is empty")
            return
        
        if self.head.next is None:
            self.head=None
            return
        
        current = self.head
        
        while current.next:
            current=current.next
            
        current.prev.next=None
        current.prev= None
        
    def remove_by_key(self,key):
        
        if self.head is None:
            print("list is empty")
            return
        
        # if self.head.next is None:
        #     self.head=None
        #     return
        
        current=self.head
        
        while current is not None and current.data !=key:
            current=current.next

            
        if current is None:
            print("key not found")
            return
        
        if self.head.data == key:
            self.remove_at_begin()
            return
        
        
        if current.next is None :
            self.remove_at_end()
            return 
        
        
        
        
        current.prev.next=current.next
        current.next.prev=current.prev
            
        
        
        
                
            

        
        
    def traverse(self):
        current = self.head
        
        while current:
            print(current.data,end="-->")
            current=current.next
    # def backward_traverse(self):
    #     if self.head is None:
    #         print("List is Empty")
    #         return
    #     current=self.head
        
    #     while current.next:
    #         current=current.next
        
    #     while current:
    #         print(current.data)
    #         current=current.prev
            
                  
n1=DoublyLinkedlist()
n1.add_at_begin(10)
n1.add_at_begin(20)
n1.add_at_begin(30)
# n1.traverse()
# n1.backward_traverse()
n1.add_at_position(100,20)
# n1.remove_at_begin()
# n1.remove_at_end()
n1.remove_by_key(100)
n1.remove_by_key(10)
n1.traverse()
