# ============================================================
#      PYTHON DATA STRUCTURES - PRACTICE QUESTIONS
#         Topics: List, Tuple, Set, Dictionary, Stack,
#                 Queue, Linked List, Tree, Graph
#                  (Easy → Medium → Hard)
# ============================================================


# ─────────────────────────────────────────────
#  LEVEL 1 : EASY
# ─────────────────────────────────────────────

# --- LISTS ---

# Q1.  Create a list of 5 fruits and print each one using a for loop.

# fruits = ["apple","orange","banana"]

# for i in fruits:
#     print(i, end="--")
# print("\n")

# Q2.  Write a function that takes a list and returns it in reversed order
#      WITHOUT using the built-in reverse() or [::-1].

# list = [1,2,3,4,5,6]

# for i in range(len(list),0,-1):
#     print(i, end="--")
# print("\n")

# Q3.  Write a function that returns the sum of all elements in a list
#      WITHOUT using sum().
# def sum_of_list(list):
#     add = 0
#     for i in list:
#         add+=i
#     print(add)
    
# sum_of_list([1,2,3,4])

# Q4.  Write a function that takes a list of numbers and returns a new
#      list containing only the even numbers.

# def new_list(list):
#     new=[]
#     for i in list:
#         if i%2==0:
#             new.append(i)
#     print(new)
            
# new_list([1,2,3,4,5,6,7,8,9,])
            



# Q5.  Write a function that removes all occurrences of a given value
#      from a list.
#      Example: remove_all([1, 2, 3, 2, 4, 2], 2) → [1, 3, 4]


# def remove(list, n):
#     new = []

#     for i in list:
#         if i!=n:
#             new.append(i)
#         else:
#             pass
#     print(new)
    
# remove([1,2,4,3,3,2,4,6,8,9,2,4,2,5,6,2,],2)
            
            
# --- TUPLES ---

# Q6.  Create a tuple of 5 numbers. Try to change one element.
#      What happens? Write a comment explaining why.
# it can't be changed because tuples are immutable


# Q7.  Write a function that swaps two variables using tuple packing/unpacking.
#      Example: swap(3, 7) → (7, 3)

def swap(tuple):
    

# Q8.  Write a function that takes a list of tuples (name, age) and
#      returns only the names.
#      Example: get_names([("Alice", 25), ("Bob", 30)]) → ["Alice", "Bob"]
 def names(tuple):
     

# --- SETS ---

# Q9.  Write a function that takes two lists and returns their
#      common elements (intersection) using sets.
#      Example: common([1,2,3,4], [3,4,5,6]) → {3, 4}

# Q10. Write a function that removes duplicate elements from a list
#      using a set and returns a sorted list.
#      Example: unique_sorted([3,1,2,1,3]) → [1, 2, 3]


# --- DICTIONARIES ---

# Q11. Write a function that counts the frequency of each character
#      in a string and returns a dictionary.
#      Example: char_freq("hello") → {'h':1, 'e':1, 'l':2, 'o':1}

# Q12. Write a function that takes a dictionary and returns a new
#      dictionary with keys and values swapped.
#      Example: swap_dict({'a': 1, 'b': 2}) → {1: 'a', 2: 'b'}

# Q13. Write a function that merges two dictionaries. If a key exists
#      in both, keep the value from the second dictionary.
#      Example: merge({'a':1,'b':2}, {'b':3,'c':4}) → {'a':1,'b':3,'c':4}


# ─────────────────────────────────────────────
#  LEVEL 2 : MEDIUM
# ─────────────────────────────────────────────

# --- LISTS ---

# Q14. Write a function that rotates a list to the left by k positions.
#      Example: rotate_left([1,2,3,4,5], 2) → [3,4,5,1,2]

# Q15. Write a function that finds the second largest element in a list
#      WITHOUT using sort() or max().

# Q16. Write a function that flattens a 2D matrix (list of lists) into
#      a single list.
#      Example: flatten([[1,2],[3,4],[5,6]]) → [1,2,3,4,5,6]


# --- STACK ---
# A Stack follows LIFO (Last In, First Out) principle.
# Implement using a Python list.

# Q17. Implement a Stack class with the following methods:
#      - push(item)   → add item to top
#      - pop()        → remove and return top item
#      - peek()       → return top item without removing
#      - is_empty()   → return True if stack is empty
#      - size()       → return number of elements

# Q18. Using your Stack, write a function is_balanced(s) that checks
#      if brackets in a string are balanced.
#      Example: is_balanced("({[]})") → True
#               is_balanced("({[})") → False


# --- QUEUE ---
# A Queue follows FIFO (First In, First Out) principle.
# Implement using a Python list.

# Q19. Implement a Queue class with the following methods:
#      - enqueue(item) → add item to rear
#      - dequeue()     → remove and return front item
#      - front()       → return front item without removing
#      - is_empty()    → return True if queue is empty
#      - size()        → return number of elements


# --- DICTIONARIES ---

# Q20. Write a function that groups a list of words by their first letter
#      and returns a dictionary.
#      Example: group_by_letter(["apple","ant","ball","bat","cat"])
#               → {'a': ['apple','ant'], 'b': ['ball','bat'], 'c': ['cat']}

# Q21. Write a function top_n(d, n) that returns the top n keys from a
#      dictionary sorted by their values (highest first).
#      Example: top_n({'a':3,'b':1,'c':5,'d':2}, 2) → ['c', 'a']


# --- LINKED LIST ---

# Q22. Implement a singly Linked List with:
#      - append(data)    → add node at the end
#      - display()       → print all node values
#      - length()        → return number of nodes

# Q23. Write a function to search for a value in the linked list.
#      Return True if found, False otherwise.


# ─────────────────────────────────────────────
#  LEVEL 3 : HARD
# ─────────────────────────────────────────────

# --- LINKED LIST ---

# Q24. Write a function to reverse a linked list in-place.
#      Example: 1 → 2 → 3 → 4 → None  becomes  4 → 3 → 2 → 1 → None

# Q25. Write a function to detect if a linked list has a cycle (loop).
#      Use Floyd's Cycle Detection Algorithm (two pointers).


# --- STACK / QUEUE ---

# Q26. Implement a Queue using two Stacks.
#      The enqueue and dequeue operations should work correctly
#      using only stack push/pop operations.

# Q27. Write a function evaluate_postfix(expression) that evaluates
#      a postfix (Reverse Polish Notation) expression using a stack.
#      Example: "3 4 + 2 *" → (3+4)*2 → 14


# --- BINARY TREE ---

# Q28. Implement a Binary Search Tree (BST) with:
#      - insert(value)      → insert a value
#      - search(value)      → return True if value exists
#      - inorder()          → return list of values in sorted order


# Q29. Write a recursive function height(node) that returns the
#      height of a binary tree.
#      (Height = number of edges on longest path from root to leaf)


# --- GRAPH ---

# Q30. Represent a graph using an adjacency list (dictionary).
#      Then implement:
#      - add_edge(u, v)     → add undirected edge between u and v
#      - bfs(start)         → Breadth First Search, return visited order
#      - dfs(start)         → Depth First Search, return visited order


# ─────────────────────────────────────────────
#  BONUS CHALLENGES
# ─────────────────────────────────────────────

# B1. Write a function that finds the longest consecutive sequence
#     in an unsorted list using a set for O(n) time.
#     Example: [100,4,200,1,3,2] → 4  (sequence: 1,2,3,4)

# B2. Implement an LRU Cache (Least Recently Used) using a dictionary
#     and a doubly linked list (or use collections.OrderedDict).
#     Support get(key) and put(key, value) with a given capacity.

# B3. Write a function to find the kth largest element in a list
#     WITHOUT fully sorting it. Use a min-heap (heapq module).

# B4. Given a list of intervals, write a function merge_intervals(intervals)
#     that merges all overlapping intervals.
#     Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

# B5. Implement a Trie (prefix tree) with:
#     - insert(word)
#     - search(word)       → True if word exists
#     - starts_with(prefix) → True if any word starts with prefix