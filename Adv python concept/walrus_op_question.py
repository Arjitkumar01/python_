# ============================================================
#        WALRUS OPERATOR ( := ) — PRACTICE QUESTIONS
#                  (Easy → Medium → Hard)
# ============================================================

# ── WHAT IS THE WALRUS OPERATOR? ─────────────────────────────
#
#  The Walrus Operator (:=) is also called the
#  "Assignment Expression" operator.
#  Introduced in Python 3.8
#
#  It lets you ASSIGN a value to a variable AND USE it
#  in the same expression — at the same time.
#
#  SYNTAX:
#       variable := expression
#
#  NORMAL WAY:
#       n = len(data)
#       if n > 10:
#           print(n)
#
#  WITH WALRUS:
#       if (n := len(data)) > 10:
#           print(n)
#
#  Common use cases:
#    → while loops
#    → if conditions
#    → list comprehensions
#    → reading input
#    → avoiding repeated function calls
# ─────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────
#  LEVEL 1 : EASY
# ─────────────────────────────────────────────

# Q1.  Without using walrus operator, the following code checks
#      the length of a list:
#
#        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#        length = len(data)
#        if length > 5:
#            print(f"List is long: {length} elements")
#
#      Rewrite the above using the walrus operator in ONE if statement.

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if (length:=len(data)>5):
#     print(f"List is long: {length} elements")

# Q2.  Rewrite the following using the walrus operator:
#
#        name = input("Enter your name: ")
#        if name != "":
#            print(f"Hello, {name}!")
#        else:
#            print("No name entered.")

# if (name:=input("enter your name:")) != "":
#     print(f"Hello, {name}!")
# else:
#     print("No name entered.")

# Q3.  The following while loop reads numbers from a list one by one
#      and stops when it finds a number greater than 8:
#
#        numbers = [2, 5, 3, 9, 1, 7]
#        index = 0
#        while index < len(numbers):
#            num = numbers[index]
#            if num > 8:
#                print(f"Found: {num}")
#                break
#            index += 1
#
#      Rewrite using walrus operator to simplify the num assignment.

# numbers = [2, 5, 3, 9, 1, 7]
# index = 0
# while index < len(numbers):
#         #    num = numbers[index]
#     if (num:=numbers[index]) > 8:
#         print(f"Found: {num}")
#         break
#     index += 1

# Q4.  Use the walrus operator to keep asking the user to enter
#      a number until they enter 0. Print each number as they enter.
#      (Simulate with a list instead of real input)
#      Hint: use a while loop with := inside the condition.


# numbers = [1,2,4,5,8,0,4]
# index=0
# while index <len(numbers):
    
#     if (num:=numbers[index]) == 0 :
        
#         break
#     else:
#         print(f"you entered {num}")
#         index+=1
        



# Q5.  Rewrite this code using walrus operator:
#
#        import re
#        text = "My phone number is 9876543210"
#        match = re.search(r'\d{10}', text)
#        if match:
#            print(f"Found number: {match.group()}")

import re
    #    text = "My phone number is 9876543210"
match = re.search(r'\d{10}', text:= "My phone number is 9876543210")
if match:
    print(f"Found number: {match.group()}")


# Q6.  Given a list of strings, use the walrus operator inside
#      a list comprehension to get only strings whose length > 4,
#      and store the length alongside the word.
#      words = ["hi", "hello", "hey", "python", "ok", "world"]
#      Expected: [('hello', 5), ('python', 6), ('world', 5)]




# Q7.  Rewrite the following WITHOUT adding extra lines —
#      use walrus to assign and check in one go:
#
#        total = sum([10, 20, 30, 40])
#        if total > 50:
#            print(f"Total is {total}, which is greater than 50")

# total = sum([10, 20, 30, 40])
if (total:= sum([10, 20, 30, 40])) > 50:
    print(f"Total is {total}, which is greater than 50")
# Q8.  Use walrus operator to read lines from a list (simulating
#      reading from a file) and print each line until an empty
#      string "" is encountered.
#      lines = ["Hello", "World", "Python", "", "Walrus"]

# Q9.  Without walrus:
#        val = some_dict.get("score")
#        if val is not None:
#            print(f"Score is {val}")
#
#      Rewrite using walrus operator.
#      Use: some_dict = {"name": "Arjit", "score": 95}

# Q10. Given a list of numbers, use walrus in a while loop
#      to pop elements one by one and print them until the
#      list is empty.
#      numbers = [10, 20, 30, 40, 50]
#      Hint: while (n := numbers.pop()) if numbers else break


# ─────────────────────────────────────────────
#  LEVEL 2 : MEDIUM
# ─────────────────────────────────────────────

# Q11. Use walrus operator inside a list comprehension to:
#      - Square each number from a list
#      - Include the result only if the square is greater than 20
#      - Return a list of (original, square) tuples
#      numbers = [1, 2, 3, 4, 5, 6]
#      Expected: [(3, 9)? No — Expected: [(5, 25), (6, 36)] ← squares > 20]
#      Wait — recalculate:
#        1²=1, 2²=4, 3²=9, 4²=16, 5²=25, 6²=36
#      Expected: [(5, 25), (6, 36)]

# Q12. Rewrite the following function using walrus operator to
#      avoid calling expensive_check() twice:
#
#        def process(data):
#            if expensive_check(data) > 100:
#                return expensive_check(data) * 2
#            return 0
#
#        def expensive_check(data):
#            return sum(data)
#
#      Rewrite process() so expensive_check() is called only ONCE.

# Q13. Use walrus operator to find the FIRST word in a list
#      that starts with the letter 'p' (case-insensitive).
#      Print it if found, else print "Not found".
#      words = ["apple", "banana", "Python", "cherry", "Pear"]

# Q14. Given a list of dictionaries (students), use walrus inside
#      a loop to find the first student whose score >= 90
#      and print their name and score.
#      students = [
#          {"name": "Arjit", "score": 85},
#          {"name": "Rahul", "score": 92},
#          {"name": "Priya", "score": 78},
#      ]

# Q15. Use the walrus operator with a while loop to simulate
#      processing a queue (list). Dequeue (pop from front) items
#      one by one and process them until the queue is empty.
#      queue = ["task1", "task2", "task3", "task4"]
#      (Use list.pop(0) to dequeue)

# Q16. Rewrite this without the temporary variable using walrus:
#
#        data = "  hello world  "
#        stripped = data.strip()
#        if len(stripped) > 5:
#            print(f"Long text: '{stripped}'")

# Q17. Use walrus operator inside a list comprehension to filter
#      and transform — get filenames that end with '.py' and
#      return their names WITHOUT the extension.
#      files = ["main.py", "README.md", "utils.py", "data.csv", "app.py"]
#      Expected: ["main", "utils", "app"]

# Q18. Use walrus to validate user input in a simulated loop.
#      Keep "asking" (iterating over a list of inputs) until a
#      valid email is entered (contains '@' and '.').
#      inputs = ["arjit", "test@", "hello.com", "arjit@gmail.com", "done"]
#      Stop and print the valid email when found.

# Q19. Use walrus operator to build a running total:
#      Given numbers = [10, 15, 20, 25, 30], use walrus inside
#      a list comprehension to create a list of cumulative sums.
#      Expected: [10, 25, 45, 70, 100]
#      Hint: Use a mutable container (list) to hold the total.

# Q20. Rewrite the following chunk-reading simulation using walrus:
#
#        data = list(range(1, 21))   # 20 elements
#        chunk_size = 4
#        while True:
#            chunk = data[:chunk_size]
#            data  = data[chunk_size:]
#            if not chunk:
#                break
#            print(f"Processing chunk: {chunk}")


# ─────────────────────────────────────────────
#  LEVEL 3 : HARD
# ─────────────────────────────────────────────

# Q21. Use walrus inside a nested list comprehension to:
#      - Given a list of sentences, extract all words longer than 5 chars
#      - Store as a flat list of (word, length) tuples
#      sentences = ["Python is powerful", "Walrus operator is amazing", "Code is fun"]
#      Expected: [('Python', 6), ('powerful', 8), ('operator', 8), ('amazing', 7)]

# Q22. Implement a simple tokenizer using walrus:
#      Given a string, repeatedly find the NEXT word using re.match()
#      or string methods in a while loop. Strip the matched word and
#      continue until the string is empty.
#      text = "walrus operator python three eight"
#      Print each token on a new line.

# Q23. Use walrus in a generator expression to lazily process and
#      filter a large sequence:
#      Given range(1, 101), use a generator with walrus to yield
#      only numbers where (n ** 2) % 7 == 0, along with their square.
#      Collect the first 5 such (n, n²) pairs.

# Q24. Combine walrus with any() and all():
#      a) Use walrus + any() to find the first number in a list
#         that is divisible by both 3 and 5.
#         numbers = [4, 7, 11, 15, 22, 30, 45]
#      b) Use walrus + all() to check if every word in a list
#         has length > 3, and store the shortest word length found.
#         words = ["Python", "code", "runs", "fast"]

# Q25. Use walrus operator inside a dictionary comprehension:
#      Given a list of words, create a dict where the key is the word
#      and value is (length, is_palindrome).
#      Use walrus to compute length once and reuse it.
#      words = ["level", "hello", "radar", "world", "civic"]
#      Expected: {'level': (5, True), 'hello': (5, False), ...}

# Q26. Write a function safe_divide_all(numbers, divisors) that
#      pairs each number with each divisor and uses walrus inside
#      a list comprehension to compute the result only if divisor != 0,
#      and includes the result in the output only if result > 1.
#      numbers = [10, 5, 20]
#      divisors = [0, 2, 3]

# Q27. Simulate a retry mechanism using walrus:
#      You have a function attempt() that returns either a result
#      or None (simulate with a list of attempts).
#      Use a while loop with walrus to keep retrying until a
#      non-None result is obtained or attempts run out.
#      attempts = [None, None, "success", "ignored"]

# Q28. Use walrus inside a comprehension to flatten and filter
#      a nested structure in one pass:
#      data = [[1, -2, 3], [-4, 5, -6], [7, 8, -9]]
#      Get all positive numbers with their (row, col) position.
#      Expected: [(0,0,1), (0,2,3), (1,1,5), (2,0,7), (2,1,8)]

# Q29. Combine walrus with a custom iterator class:
#      Create a class DataStream that yields values from a list.
#      Use walrus in a while loop to consume the stream:
#        while (value := stream.next_value()) is not None:
#            process and print value
#      The class should return None when exhausted.

# Q30. Real-world simulation — log parser:
#      Given a list of log strings, use walrus to:
#      - Parse each line with re.match()
#      - Extract (timestamp, level, message) only for "ERROR" level logs
#      - Store results in a list using list comprehension with walrus
#
#      logs = [
#          "2025-01-01 INFO Server started",
#          "2025-01-01 ERROR Disk full",
#          "2025-01-02 WARNING Low memory",
#          "2025-01-02 ERROR Connection timeout",
#          "2025-01-03 INFO Backup complete",
#      ]
#      Expected output:
#        [('2025-01-01', 'ERROR', 'Disk full'),
#         ('2025-01-02', 'ERROR', 'Connection timeout')]


# ─────────────────────────────────────────────
#  BONUS : TRICKY BEHAVIOUR
# ─────────────────────────────────────────────

# B1.  What is the output of the following? Explain why:
#
#        numbers = [y := 5, y + 1, y + 2]
#        print(numbers)
#        print(y)

# B2.  What is wrong with this code? Fix it:
#
#        if x := 10:
#            print(x)
#        # NameError or valid? Explain.

# B3.  Can you use walrus in a regular assignment? What happens?
#
#        x := 5          # Is this valid?
#        print(x)
#
#      Try it and explain the error.

# B4.  What is the output? Explain the scoping behaviour:
#
#        result = [(last := x) for x in range(5)]
#        print(result)
#        print(last)     # Is 'last' accessible here?

# B5.  Spot the difference — which is more efficient and why?
#
#        # Version A
#        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#        evens = [x for x in data if x % 2 == 0]
#        squared_evens = [x**2 for x in evens]
#
#        # Version B
#        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#        squared_evens = [s for x in data if x % 2 == 0 if (s := x**2)]
#
#        # Are they equivalent? Which is better? Why?


# ─────────────────────────────────────────────
#  QUICK REFERENCE
# ─────────────────────────────────────────────
#  Syntax     :  name := expression
#  Introduced :  Python 3.8+
#  Use in     :  if, while, comprehensions, any(), all()
#  Cannot use :  standalone statement (x := 5 alone is invalid)
#                f-strings directly, annotations
#
#  KEY BENEFIT: Avoids calling the same function/expression twice
#               and reduces temporary variables.
