# ============================================================
#        LINEAR SEARCH & BINARY SEARCH - QUESTIONS
#                  (Easy → Medium → Hard)
# ============================================================


# ── WHAT IS LINEAR SEARCH? ───────────────────────────────────
# Linear Search checks each element one by one from the start
# until the target is found or the list ends.
#
# Time Complexity : O(n)  → worst case checks all elements
# Works on        : Sorted AND unsorted arrays
# ─────────────────────────────────────────────────────────────

# ── WHAT IS BINARY SEARCH? ───────────────────────────────────
# Binary Search repeatedly divides the search space in half.
# It compares the target with the middle element and decides
# whether to search left or right.
#
# Time Complexity : O(log n)  → much faster than linear
# Works on        : SORTED arrays ONLY
# ─────────────────────────────────────────────────────────────


# ════════════════════════════════════════════
#          PART 1 : LINEAR SEARCH
# ════════════════════════════════════════════

# ── EASY ─────────────────────────────────────────────────────

# Q1.  Write a function linear_search(arr, target) that returns
#      the INDEX of the target if found, else returns -1.
#      Example:
#        linear_search([10, 30, 20, 50, 40], 20) → 2
#        linear_search([10, 30, 20, 50, 40], 99) → -1

# Q2.  Write a function is_present(arr, target) that returns
#      True if target exists in the array, False otherwise.
#      (Use linear search — do NOT use the 'in' keyword)
#      Example:
#        is_present([5, 3, 8, 1], 3) → True
#        is_present([5, 3, 8, 1], 7) → False

# Q3.  Write a function search_and_print(arr, target) that:
#      - Prints "Found at index X" if target is found
#      - Prints "Not found" if target is not in the array
#      Example:
#        search_and_print([4, 2, 7, 1, 9], 7) → Found at index 2
#        search_and_print([4, 2, 7, 1, 9], 5) → Not found

# Q4.  Write a function count_occurrences(arr, target) that
#      returns the total number of times the target appears
#      in the array using linear search.
#      Example:
#        count_occurrences([1, 2, 3, 2, 4, 2, 5], 2) → 3

# Q5.  Write a function find_all_indexes(arr, target) that
#      returns a LIST of all indexes where the target is found.
#      Example:
#        find_all_indexes([5, 3, 5, 8, 5], 5) → [0, 2, 4]
#        find_all_indexes([1, 2, 3], 9)        → []


# ── MEDIUM ────────────────────────────────────────────────────

# Q6.  Write a function linear_search_2d(matrix, target) that
#      searches for a target in a 2D list (matrix) using
#      linear search and returns (row, col) if found, else (-1, -1).
#      Example:
#        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#        linear_search_2d(matrix, 5) → (1, 1)
#        linear_search_2d(matrix, 10) → (-1, -1)

# Q7.  Write a function find_max_linear(arr) that returns the
#      MAXIMUM element and its INDEX using linear search.
#      Do NOT use max() or sort().
#      Example:
#        find_max_linear([3, 7, 1, 9, 4]) → (9, 3)
#                                             value, index

# Q8.  Write a function find_min_linear(arr) that returns the
#      MINIMUM element and its INDEX using linear search.
#      Do NOT use min() or sort().
#      Example:
#        find_min_linear([3, 7, 1, 9, 4]) → (1, 2)

# Q9.  Write a function search_in_strings(arr, target) that
#      performs a case-insensitive linear search on a list
#      of strings and returns the index if found, else -1.
#      Example:
#        search_in_strings(["Apple", "Banana", "Mango"], "banana") → 1

# Q10. Write a function find_first_even(arr) that returns the
#      FIRST even number found in the array using linear search.
#      Return -1 if no even number exists.
#      Example:
#        find_first_even([3, 7, 5, 8, 2]) → 8


# ── HARD ──────────────────────────────────────────────────────

# Q11. Write a function linear_search_recursive(arr, target, index=0)
#      that searches for target using RECURSION (no loops).
#      Return the index if found, else -1.
#      Example:
#        linear_search_recursive([10, 20, 30, 40], 30) → 2

# Q12. Write a function search_by_key(list_of_dicts, key, value)
#      that searches a list of dictionaries and returns the
#      FIRST dictionary where dict[key] == value.
#      Return None if not found.
#      Example:
#        students = [
#            {"name": "Arjit", "age": 20},
#            {"name": "Rahul", "age": 22},
#            {"name": "Priya", "age": 19}
#        ]
#        search_by_key(students, "name", "Rahul")
#        → {"name": "Rahul", "age": 22}

# Q13. Write a function find_pair_with_sum(arr, target_sum) that
#      finds the FIRST pair of elements that add up to target_sum
#      using linear search (nested loop).
#      Return the pair as a tuple, or None if no pair exists.
#      Example:
#        find_pair_with_sum([1, 4, 3, 6, 2], 7) → (4, 3)  or (1, 6)


# ════════════════════════════════════════════
#          PART 2 : BINARY SEARCH
# ════════════════════════════════════════════

# ── EASY ─────────────────────────────────────────────────────

# Q14. Write a function binary_search(arr, target) using a LOOP
#      (iterative approach) that returns the index of target
#      in a SORTED array, else returns -1.
#      Example:
#        binary_search([1, 3, 5, 7, 9, 11], 7)  → 3
#        binary_search([1, 3, 5, 7, 9, 11], 4)  → -1

# Q15. Write a function binary_search_recursive(arr, target)
#      that implements binary search using RECURSION.
#      Example:
#        binary_search_recursive([2, 5, 8, 12, 16, 23], 12) → 3

# Q16. Write a function count_steps(arr, target) that performs
#      binary search and also COUNTS how many comparisons
#      (steps) were made before finding the target or stopping.
#      Example:
#        count_steps([1,2,3,4,5,6,7,8,9,10], 7) → Found at index 6, Steps: 3

# Q17. Write a function binary_search_range(arr, target, low, high)
#      that searches only within the given index range [low, high].
#      Example:
#        binary_search_range([1,3,5,7,9,11,13,15], 9, 0, 4) → 4
#        binary_search_range([1,3,5,7,9,11,13,15], 9, 5, 7) → -1


# ── MEDIUM ────────────────────────────────────────────────────

# Q18. Write a function find_first_occurrence(arr, target) that
#      returns the index of the FIRST occurrence of target in
#      a sorted array that may have duplicates.
#      Example:
#        find_first_occurrence([1, 2, 2, 2, 3, 4], 2) → 1

# Q19. Write a function find_last_occurrence(arr, target) that
#      returns the index of the LAST occurrence of target in
#      a sorted array that may have duplicates.
#      Example:
#        find_last_occurrence([1, 2, 2, 2, 3, 4], 2) → 3

# Q20. Write a function find_insert_position(arr, target) that
#      returns the index where target SHOULD be inserted in a
#      sorted array to keep it sorted (even if target not present).
#      Example:
#        find_insert_position([1, 3, 5, 7, 9], 6) → 3
#        find_insert_position([1, 3, 5, 7, 9], 0) → 0

# Q21. Write a function search_rotated_array(arr, target) that
#      searches for target in a ROTATED sorted array.
#      Example:
#        arr = [6, 7, 8, 1, 2, 3, 4, 5]   ← rotated
#        search_rotated_array(arr, 3) → 5
#        search_rotated_array(arr, 9) → -1

# Q22. Write a function find_square_root(n) that finds the
#      integer square root of n using binary search.
#      (Return the largest integer whose square ≤ n)
#      Example:
#        find_square_root(25) → 5
#        find_square_root(20) → 4   (since 4² = 16 ≤ 20 < 25 = 5²)


# ── HARD ──────────────────────────────────────────────────────

# Q23. Write a function find_peak_element(arr) that finds a
#      PEAK element (an element greater than its neighbors)
#      using binary search.
#      Return the index of any peak element.
#      Example:
#        find_peak_element([1, 3, 5, 4, 2]) → 2  (element 5)
#        find_peak_element([1, 2, 3, 1])    → 2  (element 3)

# Q24. Write a function find_missing_number(arr) that finds
#      the one missing number in a sorted array of consecutive
#      integers using binary search.
#      Example:
#        find_missing_number([1, 2, 3, 5, 6, 7]) → 4

# Q25. Write a function search_2d_sorted_matrix(matrix, target)
#      that searches in a matrix where:
#      - Each row is sorted left to right
#      - First element of each row > last element of previous row
#      Use binary search treating the matrix as a flat array.
#      Return True if found, False otherwise.
#      Example:
#        matrix = [[1,3,5],[7,9,11],[13,15,17]]
#        search_2d_sorted_matrix(matrix, 9)  → True
#        search_2d_sorted_matrix(matrix, 10) → False


# ─────────────────────────────────────────────
#  COMPARISON TABLE
# ─────────────────────────────────────────────
#
#  Feature          | Linear Search  | Binary Search
#  -----------------|----------------|------------------
#  Array type       | Any (unsorted) | Must be SORTED
#  Time complexity  | O(n)           | O(log n)
#  Space complexity | O(1)           | O(1) iterative
#                   |                | O(log n) recursive
#  Best case        | O(1)           | O(1)
#  Approach         | Check one by   | Divide & conquer
#                   | one            |
#  Use when         | Small / unsorted| Large sorted arrays
#
# ───────────────────────────────────


# arr = [1,2,3,4,5]

# old_value=32
# new_value=30
# n=len(arr)

# for i in range(n):
#     if arr[i]==old_value:
#         arr[i]=new_value
#         break
# else:
#     print("element not found")
# print(arr)

arr=[11,22,44,5,99,666,55]
minimum=arr[0]
maximum=arr[0]

for i in range(1,len(arr)):
    if minimum>arr[i]:
        minimum=arr[i]
print("minimum:",minimum)

for i in range(1,len(arr)):
    if maximum<arr[i]:
        maximum=arr[i]
print("maximum:",maximum)

