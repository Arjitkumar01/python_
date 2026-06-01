# ============================================================
#         PYTHON FUNCTIONS - PRACTICE QUESTIONS
#                  (Easy → Medium → Hard)
# ============================================================


# ─────────────────────────────────────────────
#  LEVEL 1 : EASY
# ─────────────────────────────────────────────

# Q1. Write a function greet() that prints "Hello, World!"

# def greet():
#     print("Hello, World!")
# greet()



# Q2. Write a function greet_user(name) that takes a name as
#     argument and prints "Hello, <name>!"



# def greet_user(name):
#     print("Hello, "+ name +"!")
# greet_user("Arjit")

# Q3. Write a function add(a, b) that returns the sum of two numbers.

# def add(a,b):   
#     return a+b
# sum  = add(3,5)
# print(sum)

# Q4. Write a function is_even(n) that returns True if n is even,
#     False otherwise.

# def is_even(n):
#     if(n%2==0):
#         return "True"
#     else:
#         return "False"
# is_even(2)

# Q5. Write a function square(n) that returns the square of a number.

# def square(n):
#     return n*n

# square1= square(5)
# print(square1)

# Q6. Write a function max_of_two(a, b) that returns the larger number.

# def max_of_two(a,b):
#     if(a>b):
#         return "A is larger "
#     else:
#         return "B is larger"
        
# max_of_two(88,99)

# Q7. Write a function celsius_to_fahrenheit(c) that converts
#     Celsius to Fahrenheit.  Formula: F = (C × 9/5) + 32

# def celsius_to_fahrenheit(c):
#     F= (c * 9/5) + 32
    
#     return F
# Fahrenheit= celsius_to_fahrenheit(23)
# print(Fahrenheit)

# Q8. Write a function count_vowels(s) that counts and returns\
#     the number of vowels in a string.

# def count_vowels(s):
#     count=0
#     for ch in s.lower():
#         if ch in "aeiou":
#             count+=1
#     return count

# print(count_vowels("Hello arjit kumar"))


# Q9. Write a function repeat_string(s, n) that returns the
#     string s repeated n times.

# def repeat_string(s, n):
#     a= s*n
#     return a
# print(repeat_string("Baby I lovee uhh\n",5))

# Q10. Write a function is_positive(n) that returns "Positive",
#      "Negative", or "Zero" based on the value of n.

# def is_positive(n):
#     if (n==0):
#         return "Zero"
#     elif(n<0):
#         return "Negative"
#     else:
#         return "Positive"
    
# print(is_positive(34))
# print(is_positive(-34))
# print(is_positive(0))

# ─────────────────────────────────────────────
#  LEVEL 2 : MEDIUM
# ─────────────────────────────────────────────

# Q11. Write a function factorial(n) that returns the factorial
#      of n using recursion

# def factorial(n):
#     if n==1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(10))


# Q12. Write a function fibonacci(n) that returns the nth
#      Fibonacci number using recursion.


# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))

# Q13. Write a function is_palindrome(s) that returns True if
#      the string is a palindrome, False otherwise.

# def is_palindrome(s):
#     if s== s[::-1]:
#         return "True"
#     else:
#         return "False"
    
# print(is_palindrome("level"))


# Q14. Write a function find_max(lst) that returns the largest
#      element in a list WITHOUT using the built-in max().

# Q15. Write a function remove_duplicates(lst) that returns a
#      new list with duplicate elements removed.

# Q16. Write a function calculator(a, b, op) that performs
#      addition, subtraction, multiplication, or division
#      based on the op argument ('+', '-', '*', '/').

# def calculator(a , b , op):
#     if op=='+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op=='*':
#         return a*b
#     elif op=='/':
#         return a/b
    
# print(calculator(5,5,'/'))
    

# Q17. Write a function count_words(sentence) that returns the
#      number of words in a sentence.

def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("Hey arjit how are you"))


# Q18. Write a function power(base, exp) that calculates base^exp
#      using recursion (without using ** operator).

# Q19. Write a function flatten(lst) that takes a nested list
#      like [1, [2, 3], [4, [5]]] and returns [1, 2, 3, 4, 5].

# Q20. Write a function apply_twice(func, value) that takes a
#      function and a value, applies the function twice, and
#      returns the result.
#      Example: apply_twice(square, 3) → square(square(3)) → 81


# ─────────────────────────────────────────────
#  LEVEL 3 : HARD
# ─────────────────────────────────────────────

# Q21. Write a function memoize(func) that takes a function and
#      returns a new function that caches (stores) results of
#      previous calls to avoid recomputation.

# Q22. Write a function make_counter() that returns a counter
#      function. Each time the returned function is called,
#      it should return an incrementing count (1, 2, 3, ...).
#      Use closures — no classes allowed.

# Q23. Write a function sort_by_frequency(lst) that sorts a list
#      of elements by their frequency (most frequent first).
#      Example: [1, 3, 2, 1, 3, 1] → [1, 1, 1, 3, 3, 2]

# Q24. Write a function curry_add(a) that returns a function
#      which takes b and returns a + b.
#      Example: add5 = curry_add(5); add5(3) → 8
#      Extend it: curry_add(1)(2)(3) should return 6.

# Q25. Write a function compose(*funcs) that takes multiple
#      functions and returns a new function that applies them
#      from right to left.
#      Example: compose(double, increment)(5) → double(increment(5)) → 12

# Q26. Write a recursive function binary_search(lst, target)
#      that returns the index of target in a sorted list,
#      or -1 if not found.

# Q27. Write a function group_by(lst, key_func) that groups
#      elements of a list by the result of key_func.
#      Example: group_by([1,2,3,4,5], lambda x: x%2)
#               → {1: [1,3,5], 0: [2,4]}

# Q28. Write a generator function infinite_counter(start=0)
#      that yields numbers starting from `start` indefinitely.
#      Then write a function take(n, gen) that returns the
#      first n values from a generator.

# Q29. Write a decorator log_calls that prints the function
#      name, arguments, and return value every time a
#      decorated function is called.

# Q30. Write a function deep_flatten(lst) that flattens a
#      deeply nested list of any depth using recursion.
#      Example: [1, [2, [3, [4, [5]]]]] → [1, 2, 3, 4, 5]


# ─────────────────────────────────────────────
#  BONUS : LAMBDA CHALLENGES
# ─────────────────────────────────────────────

# B1. Use a lambda to sort a list of tuples by the second element.
#     lst = [(1, 3), (4, 1), (2, 2)]  →  [(4,1), (2,2), (1,3)]

# B2. Use a lambda with filter() to get all even numbers from a list.

# B3. Use a lambda with map() to convert a list of strings to uppercase.

# B4. Use a lambda with reduce() to find the product of all numbers
#     in a list.  (import functools)

# B5. Chain map() and filter() using lambdas to:
#     - filter even numbers from [1..10]
#     - then square each of them
#     Expected: [4, 16, 36, 64, 100]



#                                 <-----ANSWERS----->


