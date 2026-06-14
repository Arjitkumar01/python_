# ============================================================
#      PYTHON DATA STRUCTURES - ANSWERS
#         Topics: List, Tuple, Set, Dictionary, Stack,
#                 Queue, Linked List, Tree, Graph
#                  (Easy → Medium → Hard)
# ============================================================


# ─────────────────────────────────────────────
#  LEVEL 1 : EASY
# ─────────────────────────────────────────────

# Q1. Create a list of 5 fruits and print each one
fruits = ["apple", "banana", "cherry", "mango", "grape"]
for fruit in fruits:
    print(fruit)


# Q2. Reverse a list without reverse() or [::-1]
def reverse_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

print(reverse_list([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]


# Q3. Sum of all elements without sum()
def list_sum(lst):
    total = 0
    for item in lst:
        total += item
    return total

print(list_sum([1, 2, 3, 4, 5]))   # 15


# Q4. Return only even numbers from a list
def get_evens(lst):
    return [x for x in lst if x % 2 == 0]

print(get_evens([1, 2, 3, 4, 5, 6]))   # [2, 4, 6]


# Q5. Remove all occurrences of a value from a list
def remove_all(lst, val):
    return [x for x in lst if x != val]

print(remove_all([1, 2, 3, 2, 4, 2], 2))   # [1, 3, 4]


# Q6. Tuples are immutable — trying to change an element raises TypeError
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10   # ← This would raise: TypeError: 'tuple' object does not support item assignment
# Tuples are immutable — their elements cannot be changed after creation.


# Q7. Swap two variables using tuple unpacking
def swap(a, b):
    a, b = b, a
    return (a, b)

print(swap(3, 7))   # (7, 3)


# Q8. Return only names from a list of (name, age) tuples
def get_names(lst):
    return [name for name, age in lst]

print(get_names([("Alice", 25), ("Bob", 30)]))   # ['Alice', 'Bob']


# Q9. Common elements of two lists using sets
def common(lst1, lst2):
    return set(lst1) & set(lst2)

print(common([1, 2, 3, 4], [3, 4, 5, 6]))   # {3, 4}


# Q10. Remove duplicates and return sorted list
def unique_sorted(lst):
    return sorted(set(lst))

print(unique_sorted([3, 1, 2, 1, 3]))   # [1, 2, 3]


# Q11. Character frequency dictionary
def char_freq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_freq("hello"))   # {'h':1, 'e':1, 'l':2, 'o':1}


# Q12. Swap keys and values in a dictionary
def swap_dict(d):
    return {v: k for k, v in d.items()}

print(swap_dict({'a': 1, 'b': 2}))   # {1: 'a', 2: 'b'}


# Q13. Merge two dictionaries (second wins on conflict)
def merge(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result

print(merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))   # {'a':1, 'b':3, 'c':4}


# ─────────────────────────────────────────────
#  LEVEL 2 : MEDIUM
# ─────────────────────────────────────────────

# Q14. Rotate list to the left by k positions
def rotate_left(lst, k):
    k = k % len(lst)    # handle k > len
    return lst[k:] + lst[:k]

print(rotate_left([1, 2, 3, 4, 5], 2))   # [3, 4, 5, 1, 2]


# Q15. Second largest element without sort() or max()
def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

print(second_largest([3, 1, 9, 2, 7]))   # 7


# Q16. Flatten a 2D matrix
def flatten_matrix(matrix):
    result = []
    for row in matrix:
        for item in row:
            result.append(item)
    return result

print(flatten_matrix([[1, 2], [3, 4], [5, 6]]))   # [1, 2, 3, 4, 5, 6]


# Q17. Stack implementation using a list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())     # 3
print(s.pop())      # 3
print(s.size())     # 2


# Q18. Balanced brackets checker using Stack
def is_balanced(s):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()

print(is_balanced("({[]})"))   # True
print(is_balanced("({[})"))    # False


# Q19. Queue implementation using a list
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print(q.front())    # a
print(q.dequeue())  # a
print(q.size())     # 2


# Q20. Group words by their first letter
def group_by_letter(words):
    result = {}
    for word in words:
        key = word[0]
        if key not in result:
            result[key] = []
        result[key].append(word)
    return result

print(group_by_letter(["apple", "ant", "ball", "bat", "cat"]))
# {'a': ['apple', 'ant'], 'b': ['ball', 'bat'], 'c': ['cat']}


# Q21. Top n keys by value (highest first)
def top_n(d, n):
    return sorted(d, key=lambda k: d[k], reverse=True)[:n]

print(top_n({'a': 3, 'b': 1, 'c': 5, 'd': 2}, 2))   # ['c', 'a']


# Q22. Singly Linked List implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" → ".join(str(e) for e in elements))

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()         # 1 → 2 → 3
print(ll.length())   # 3


# Q23. Search in linked list
def search_ll(linked_list, value):
    current = linked_list.head
    while current:
        if current.data == value:
            return True
        current = current.next
    return False

print(search_ll(ll, 2))   # True
print(search_ll(ll, 9))   # False


# ─────────────────────────────────────────────
#  LEVEL 3 : HARD
# ─────────────────────────────────────────────

# Q24. Reverse a linked list in-place
def reverse_ll(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

ll2 = LinkedList()
for val in [1, 2, 3, 4]:
    ll2.append(val)
ll2.display()        # 1 → 2 → 3 → 4
reverse_ll(ll2)
ll2.display()        # 4 → 3 → 2 → 1


# Q25. Detect cycle in linked list (Floyd's algorithm)
def has_cycle(linked_list):
    slow = linked_list.head
    fast = linked_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Creating a cycle for testing
ll3 = LinkedList()
ll3.append(1)
ll3.append(2)
ll3.append(3)
# Create cycle: tail points back to head
ll3.head.next.next.next = ll3.head
print(has_cycle(ll3))   # True
print(has_cycle(ll))    # False


# Q26. Queue using two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.inbox  = []   # stack for enqueue
        self.outbox = []   # stack for dequeue

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if not self.outbox:
            return "Queue is empty"
        return self.outbox.pop()

qs = QueueUsingStacks()
qs.enqueue(1)
qs.enqueue(2)
qs.enqueue(3)
print(qs.dequeue())   # 1 (FIFO)
print(qs.dequeue())   # 2


# Q27. Evaluate postfix expression using Stack
def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
    return stack[0]

print(evaluate_postfix("3 4 + 2 *"))   # 14
print(evaluate_postfix("5 1 2 + 4 * + 3 -"))   # 14


# Q28. Binary Search Tree (BST)
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return BSTNode(value)
        if value < node.value:
            node.left  = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

bst = BST()
for val in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(val)
print(bst.search(4))     # True
print(bst.search(9))     # False
print(bst.inorder())     # [1, 3, 4, 5, 6, 7, 8]


# Q29. Height of a binary tree
def height(node):
    if node is None:
        return -1   # -1 for edge count, 0 for node count
    return 1 + max(height(node.left), height(node.right))

print(height(bst.root))   # 2


# Q30. Graph with adjacency list + BFS + DFS
from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        self.adj[v].append(u)   # undirected

    def bfs(self, start):
        visited = []
        queue   = deque([start])
        seen    = {start}
        while queue:
            node = queue.popleft()
            visited.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return visited

    def dfs(self, start, visited=None, seen=None):
        if visited is None:
            visited = []
            seen    = set()
        seen.add(start)
        visited.append(start)
        for neighbor in self.adj.get(start, []):
            if neighbor not in seen:
                self.dfs(neighbor, visited, seen)
        return visited

g = Graph()
for u, v in [(1,2),(1,3),(2,4),(3,4),(4,5)]:
    g.add_edge(u, v)
print(g.bfs(1))   # [1, 2, 3, 4, 5]
print(g.dfs(1))   # [1, 2, 4, 3, 5]


# ─────────────────────────────────────────────
#  BONUS CHALLENGES
# ─────────────────────────────────────────────

# B1. Longest consecutive sequence using set (O(n))
def longest_consecutive(lst):
    num_set = set(lst)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:   # start of a sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4  (1,2,3,4)


# B2. LRU Cache using OrderedDict
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache    = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)   # remove least recently used

lru = LRUCache(3)
lru.put(1, "a")
lru.put(2, "b")
lru.put(3, "c")
lru.get(1)        # access 1 → moves to end
lru.put(4, "d")   # evicts 2 (least recently used)
print(lru.get(2)) # -1 (evicted)
print(lru.get(1)) # 'a'


# B3. Kth largest element using min-heap
import heapq

def kth_largest(lst, k):
    return heapq.nlargest(k, lst)[-1]

print(kth_largest([3, 1, 5, 12, 2, 11], 3))   # 5


# B4. Merge overlapping intervals
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
# [[1, 6], [8, 10], [15, 18]]


# B5. Trie (Prefix Tree) implementation
class TrieNode:
    def __init__(self):
        self.children  = {}
        self.is_end    = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

trie = Trie()
for word in ["apple", "app", "apt", "bat"]:
    trie.insert(word)

print(trie.search("apple"))       # True
print(trie.search("ap"))          # False
print(trie.starts_with("ap"))     # True
print(trie.starts_with("bat"))    # True
print(trie.starts_with("cat"))    # False
