# ============================================================
#         PYTHON FUNCTIONS - ANSWERS
#                  (Easy → Medium → Hard)
# ============================================================


# ─────────────────────────────────────────────
#  LEVEL 1 : EASY
# ─────────────────────────────────────────────

# Q1. Function that prints "Hello, World!"
def greet():
    print("Hello, World!")

greet()


# Q2. Function that greets a user by name
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")


# Q3. Function that returns sum of two numbers
def add(a, b):
    return a + b

print(add(3, 5))        # 8


# Q4. Function that checks if a number is even
def is_even(n):
    return n % 2 == 0

print(is_even(4))       # True
print(is_even(7))       # False


# Q5. Function that returns square of a number
def square(n):
    return n * n

print(square(6))        # 36


# Q6. Function that returns the larger of two numbers
def max_of_two(a, b):
    return a if a > b else b

print(max_of_two(10, 20))   # 20


# Q7. Celsius to Fahrenheit converter
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))     # 32.0
print(celsius_to_fahrenheit(100))   # 212.0


# Q8. Count vowels in a string
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))  # 3


# Q9. Repeat a string n times
def repeat_string(s, n):
    return s * n

print(repeat_string("ha", 3))   # hahaha


# Q10. Check if number is positive, negative, or zero
def is_positive(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(is_positive(5))    # Positive
print(is_positive(-3))   # Negative
print(is_positive(0))    # Zero


# ─────────────────────────────────────────────
#  LEVEL 2 : MEDIUM
# ─────────────────────────────────────────────

# Q11. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))     # 120
print(factorial(0))     # 1


# Q12. Fibonacci using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))     # 13
print(fibonacci(10))    # 55


# Q13. Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))     # True
print(is_palindrome("hello"))       # False
print(is_palindrome("A man a plan a canal Panama"))  # True


# Q14. Find max in a list without max()
def find_max(lst):
    maximum = lst[0]
    for item in lst:
        if item > maximum:
            maximum = item
    return maximum

print(find_max([3, 1, 9, 2, 7]))    # 9


# Q15. Remove duplicates from a list
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))    # [1, 2, 3, 4, 5]


# Q16. Calculator function
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"

print(calculator(10, 5, '+'))   # 15
print(calculator(10, 5, '-'))   # 5
print(calculator(10, 5, '*'))   # 50
print(calculator(10, 5, '/'))   # 2.0


# Q17. Count words in a sentence
def count_words(sentence):
    return len(sentence.split())

print(count_words("Hello World how are you"))   # 5


# Q18. Power using recursion (without **)
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 10))     # 1024
print(power(3, 4))      # 81


# Q19. Flatten a one-level nested list
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            for sub in item:
                result.append(sub)
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], [4, 5]]))     # [1, 2, 3, 4, 5]


# Q20. Apply a function twice
def apply_twice(func, value):
    return func(func(value))

print(apply_twice(square, 3))       # square(square(3)) = square(9) = 81
print(apply_twice(lambda x: x + 1, 5))  # 7


# ─────────────────────────────────────────────
#  LEVEL 3 : HARD
# ─────────────────────────────────────────────

# Q21. Memoize decorator using a cache dictionary
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def slow_square(n):
    return n * n

print(slow_square(10))  # 100 (computed)
print(slow_square(10))  # 100 (from cache)


# Q22. Counter using closure
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3


# Q23. Sort list by frequency (most frequent first)
def sort_by_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return sorted(lst, key=lambda x: freq[x], reverse=True)

print(sort_by_frequency([1, 3, 2, 1, 3, 1]))   # [1, 1, 1, 3, 3, 2]


# Q24. Curried add function
def curry_add(a):
    def inner(b):
        return a + b
    return inner

add5 = curry_add(5)
print(add5(3))          # 8
print(curry_add(1)(2))  # 3

# Extended: curry_add(1)(2)(3) → 6
def curry_add_ext(a):
    def inner(b):
        def innermost(c):
            return a + b + c
        return innermost
    return inner

print(curry_add_ext(1)(2)(3))   # 6


# Q25. Compose functions (right to left)
def compose(*funcs):
    def composed(value):
        for func in reversed(funcs):
            value = func(value)
        return value
    return composed

double    = lambda x: x * 2
increment = lambda x: x + 1

transform = compose(double, increment)
print(transform(5))     # double(increment(5)) = double(6) = 12


# Q26. Binary search using recursion
def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return binary_search(lst, target, low, mid - 1)

print(binary_search([1, 3, 5, 7, 9, 11], 7))   # 3
print(binary_search([1, 3, 5, 7, 9, 11], 4))   # -1


# Q27. Group list elements by a key function
def group_by(lst, key_func):
    result = {}
    for item in lst:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

print(group_by([1, 2, 3, 4, 5], lambda x: x % 2))
# {1: [1, 3, 5], 0: [2, 4]}


# Q28. Infinite counter generator + take()
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

def take(n, gen):
    result = []
    for _ in range(n):
        result.append(next(gen))
    return result

gen = infinite_counter(1)
print(take(5, gen))     # [1, 2, 3, 4, 5]


# Q29. Decorator that logs function calls
def log_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Called: {func.__name__}  |  Args: {args}  |  Returned: {result}")
        return result
    return wrapper

@log_calls
def multiply(a, b):
    return a * b

multiply(4, 5)
# Called: multiply  |  Args: (4, 5)  |  Returned: 20


# Q30. Deep flatten a nested list of any depth
def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

print(deep_flatten([1, [2, [3, [4, [5]]]]]))    # [1, 2, 3, 4, 5]
print(deep_flatten([1, [2, 3], [4, [5, [6]]]]))  # [1, 2, 3, 4, 5, 6]


# ─────────────────────────────────────────────
#  BONUS : LAMBDA CHALLENGES
# ─────────────────────────────────────────────

# B1. Sort list of tuples by second element
lst = [(1, 3), (4, 1), (2, 2)]
sorted_lst = sorted(lst, key=lambda x: x[1])
print(sorted_lst)   # [(4, 1), (2, 2), (1, 3)]


# B2. Filter even numbers using lambda + filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)        # [2, 4, 6, 8, 10]


# B3. Convert list of strings to uppercase using lambda + map()
words = ["hello", "world", "python"]
upper_words = list(map(lambda s: s.upper(), words))
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']


# B4. Product of all numbers using lambda + reduce()
from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, nums)
print(product)      # 120


# B5. Chain filter + map: filter evens from 1-10, then square them
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 11))))
print(result)       # [4, 16, 36, 64, 100]
