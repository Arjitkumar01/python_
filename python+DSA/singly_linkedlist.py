# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None


# ll = LinkedList()

# first = Node(10)
# second = Node(20)
# third = Node(30)

# ll.head = first
# first.next = second
# second.next = third
# current =first

# while current:
#     print(current.data)
#     current=current.next
    
    
    
    
    
# =========================================================================================================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linked_list:
    
    def __init__(self):
        self.head=None
        
    def Display(self):
        
        if self.head == None:
            print("List is empty")
            return
        
        current=self.head
        
        while current:
            print(current.data, end=" -> ")
            current=current.next
            
    def insert_begin(self,data):
        new_node=Node(data)
        
        new_node.next=self.head
        self.head=new_node
    
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        
        current= self.head
        
        while current.next:
            current=current.next
        current.next=new_node
        
    def insert_at_position(self,position,data):
        
        if position==0:
            self.insert_begin(data)
            return
        
        new_node=Node(data)
        
        current=self.head
        
        for i in range(position-1):
            
            if current is None:
                print("Invalid position")
                return
            current=current.next
            
        if current is None:
            print("Invalid Position")
            return
        new_node.next=current.next
        current.next=new_node
    def add_next_to_data(self,data,key):
        new_node=Node(data)
        if self.head==None:
            print("list is empty")
            
            
        current=self.head
        
        while current is not None and current.data!=key:
            current=current.next
        
        if current is None :
            print("inavalid key")
            
        new_node.next=current.next
        current.next=new_node
        
        
        
    def remove_begin(self):
        if self.head is None:
            print("Empty list")
            return
        if self.head.next is None:
            self.head = None
            return
            
        self.head=self.head.next
    def remove_end(self):
        if self.head is None:
            print("Empty list")
            return
        if self.head.next is None:
            self.head=None
            return
        current = self.head
        
        while current.next.next:
            current=current.next
        current.next=None
        
    def remove_at_position(self,position):
        if self.head == None:
            print("Linked list is empty")
            return
        if position ==0:
            self.remove_begin()
            return
        
        current =self.head
        for i in range(position-1):
            
            if current is None or current.next is None:
                print("invalid posuition")
                return
            current=current.next
            
        if current.next is None:
            print("invalid position")
            return
        
        current.next=current.next.next
        
        
    def search(self,key):
        current=self.head
        position = 0
        
        while current:
            if current.data==key:
                print("element found")
                print(f"position:{position}")
                return
            current=current.next
            position+=1
        
        print("element not found") 
        
    def count(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        count=1
        current=self.head
        while current.next:
            count+=1
            current=current.next
            
        print(f"count : {count}")
        return
    
    
    def reverse(self):
        
        current=self.head
        prev=None
        
        while current:
            new_node=current.next
            current.next=prev
            prev=current
            current=new_node
            
        self.head = prev
        

l1=Linked_list()
l1.insert_begin(101)
l1.insert_begin(202)
l1.insert_begin(303)
l1.insert_begin(404)
l1.insert_begin(505)
# l1.insert_end(202)
# l1.insert_end(303)
# l1.insert_end(404)
# l1.insert_end(505)
# l1.insert_at_position(2,111)
# l1.remove_begin()
# l1.remove_end()
# l1.remove_at_position(4)
l1.search(202)
l1.count()

l1.Display()
        
    
    