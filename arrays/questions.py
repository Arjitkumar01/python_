# =============================================================================
# PYTHON ARRAY PRACTICE QUESTIONS - 150 Questions
# =============================================================================
# Topics: Basics, Array Operations, Linear Search, Binary Search,
#         Sorting, Mixed/Advanced
# =============================================================================

# =============================================================================
# SECTION 1 - BASICS (Q1-Q20)
# =============================================================================

# Q1. Create an array (list) of 5 integers and print it.
#     Example: [] → [10, 20, 30, 40, 50]

# list=[10, 20, 30, 40, 50]
# print(list)

# Q2. Access the first, middle, and last element of a list using indexing.
#     Example: [10, 20, 30, 40, 50] → first=10, middle=30, last=50

# list= [10, 20, 30, 40, 50]
# print(list[0])
# print(list[2])
# print(list[-1])

# Q3. Use negative indexing to print the last two elements of a list.
#     Example: [10, 20, 30, 40, 50] → [40, 50]
# list=[10, 20, 30, 40, 50]
# print(list[-2:])

# Q4. Slice a list to get elements from index 1 to 3 (inclusive).
#     Example: [10, 20, 30, 40, 50] → [20, 30, 40]

list = [10, 20, 30, 40, 50]
print(list[1:3])
# Q5. Slice a list to get every other element (step = 2).
#     Example: [10, 20, 30, 40, 50] → [10, 30, 50]
list = [10, 20, 30, 40, 50]
print(list[::2])
# Q6. Modify the second element of a list and print the updated list.
#     Example: [10, 20, 30] → change index 1 to 99 → [10, 99, 30]

# Q7. Append an element to the end of a list.
#     Example: [1, 2, 3] + append(4) → [1, 2, 3, 4]

# Q8. Insert an element at a specific index in a list.
#     Example: [1, 2, 4, 5] → insert 3 at index 2 → [1, 2, 3, 4, 5]

# Q9. Remove a specific element from a list by value.
#     Example: [1, 2, 3, 4] → remove(3) → [1, 2, 4]

# Q10. Pop the last element from a list and print the popped value and the remaining list.
#      Example: [1, 2, 3, 4] → popped=4, remaining=[1, 2, 3]

# Q11. Find the length of a list using len().
#      Example: [10, 20, 30, 40] → 4

# Q12. Check if an element exists in a list using the 'in' operator.
#      Example: [1, 2, 3, 4, 5], check 3 → True; check 9 → False

# Q13. Count how many times a specific element appears in a list.
#      Example: [1, 2, 2, 3, 2, 4] → count(2) → 3

# Q14. Find the index of the first occurrence of an element in a list.
#      Example: [10, 20, 30, 20] → index(20) → 1

# Q15. Sort a list of integers in ascending order using sort().
#      Example: [5, 2, 8, 1, 9] → [1, 2, 5, 8, 9]

# Q16. Reverse a list using the reverse() method.
#      Example: [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]

# Q17. Create a copy of a list and verify they are independent (changing one doesn't affect the other).
#      Example: a=[1,2,3], b=a.copy() → modify b[0]=99 → a still [1,2,3]

# Q18. Concatenate two lists using the + operator.
#      Example: [1, 2, 3] + [4, 5, 6] → [1, 2, 3, 4, 5, 6]

# Q19. Repeat a list 3 times using the * operator.
#      Example: [1, 2] * 3 → [1, 2, 1, 2, 1, 2]

# Q20. Create a list of squares of numbers from 1 to 10 using list comprehension.
#      Then convert it to a tuple and back to a list.
#      Example: → [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# =============================================================================
# SECTION 2 - ARRAY OPERATIONS (Q21-Q40)
# =============================================================================

# Q21. Calculate the sum of all elements in a list WITHOUT using the built-in sum().
#      Example: [1, 2, 3, 4, 5] → 15

# Q22. Find the maximum element in a list WITHOUT using the built-in max().
#      Example: [3, 7, 1, 9, 4] → 9

# Q23. Find the minimum element in a list WITHOUT using the built-in min().
#      Example: [3, 7, 1, 9, 4] → 1

# Q24. Find the second largest element in a list (without sorting).
#      Example: [3, 7, 1, 9, 4] → 7

# Q25. Find the second smallest element in a list (without sorting).
#      Example: [3, 7, 1, 9, 4] → 3

# Q26. Reverse a list WITHOUT using the reverse() method or slicing [::-1].
#      Use a loop to swap elements in-place.
#      Example: [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]

# Q27. Rotate a list to the LEFT by k positions.
#      Example: [1, 2, 3, 4, 5], k=2 → [3, 4, 5, 1, 2]

# Q28. Rotate a list to the RIGHT by k positions.
#      Example: [1, 2, 3, 4, 5], k=2 → [4, 5, 1, 2, 3]

# Q29. Merge two sorted arrays into a single sorted array (without using sort()).
#      Example: [1, 3, 5] + [2, 4, 6] → [1, 2, 3, 4, 5, 6]

# Q30. Remove all duplicate elements from a list while preserving the original order.
#      Example: [1, 2, 2, 3, 4, 3, 5] → [1, 2, 3, 4, 5]

# Q31. Find all even and all odd numbers from a list and return them as two separate lists.
#      Example: [1, 2, 3, 4, 5, 6] → evens=[2,4,6], odds=[1,3,5]

# Q32. Count the number of positive and negative integers in a list.
#      Example: [1, -2, 3, -4, 0, 5] → positives=3, negatives=2, zeros=1

# Q33. Move all zeros to the end of a list while maintaining the order of non-zero elements.
#      Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

# Q34. Flatten a 2D list (list of lists) into a single 1D list.
#      Example: [[1, 2], [3, 4], [5, 6]] → [1, 2, 3, 4, 5, 6]

# Q35. Find the missing number in a list containing integers from 1 to n with one missing.
#      Example: [1, 2, 4, 5, 6] (n=6) → missing = 3

# Q36. Check if a list is sorted in ascending order. Return True or False.
#      Example: [1, 2, 3, 4, 5] → True; [1, 3, 2, 4] → False

# Q37. Find common elements between two lists (intersection) without using sets.
#      Example: [1, 2, 3, 4] and [3, 4, 5, 6] → [3, 4]

# Q38. Find the union of two lists (all unique elements from both) without using sets.
#      Example: [1, 2, 3] and [3, 4, 5] → [1, 2, 3, 4, 5]

# Q39. Find the intersection of two lists using sets.
#      Example: [1, 2, 3, 4] and [3, 4, 5, 6] → {3, 4}

# Q40. Given two lists, find elements that are in either list but NOT in both (symmetric difference).
#      Example: [1, 2, 3, 4] and [3, 4, 5, 6] → [1, 2, 5, 6]


# =============================================================================
# SECTION 3 - LINEAR SEARCH (Q41-Q60)
# =============================================================================

# Q41. Implement basic linear search: return the index of the target element.
#      Return -1 if not found.
#      Example: [10, 20, 30, 40], target=30 → 2; target=99 → -1

# Q42. Implement linear search that returns True if element is found, False otherwise.
#      Example: [5, 10, 15, 20], target=10 → True; target=7 → False

# Q43. Search for an element and print "Found at index X" or "Not found" accordingly.
#      Example: [4, 8, 12, 16], target=12 → "Found at index 2"

# Q44. Count the total number of times a target element appears in a list using linear search.
#      Example: [1, 2, 3, 2, 4, 2], target=2 → 3

# Q45. Find ALL indexes where the target element appears (return a list of indices).
#      Example: [1, 2, 3, 2, 4, 2], target=2 → [1, 3, 5]

# Q46. Find the FIRST occurrence of the target element and return its index.
#      Return -1 if not found.
#      Example: [5, 3, 5, 7, 5], target=5 → 0

# Q47. Find the LAST occurrence of the target element and return its index.
#      Return -1 if not found.
#      Example: [5, 3, 5, 7, 5], target=5 → 4

# Q48. Perform linear search on a 2D matrix (list of lists). Return (row, col) if found.
#      Example: [[1,2],[3,4],[5,6]], target=4 → (1, 1)

# Q49. Perform a case-insensitive linear search on a list of strings.
#      Example: ["Apple", "Banana", "Cherry"], target="banana" → Found at index 1

# Q50. Search for a specific value in a list of dictionaries by a given key.
#      Example: [{"name":"Alice","age":25}, {"name":"Bob","age":30}], search name="Bob" → index 1

# Q51. Find the first EVEN number in a list using linear search. Return its index.
#      Example: [1, 3, 7, 4, 9] → index 3 (value 4)

# Q52. Find the first ODD number in a list using linear search. Return its index.
#      Example: [2, 4, 6, 3, 8] → index 3 (value 3)

# Q53. Find the first NEGATIVE number in a list using linear search. Return its index.
#      Example: [5, 3, -1, 7, -4] → index 2 (value -1)

# Q54. Implement linear search RECURSIVELY. Return the index of the target or -1.
#      Example: [10, 20, 30, 40, 50], target=30 → 2

# Q55. Find a pair of elements that add up to a given target sum using a nested loop (brute force).
#      Example: [2, 4, 3, 5, 7], target=9 → (4, 5) or (2, 7)

# Q56. Find the maximum element in a list using linear search and also return its index.
#      Example: [3, 9, 1, 7, 5] → max=9, index=1

# Q57. Find the minimum element in a list using linear search and also return its index.
#      Example: [3, 9, 1, 7, 5] → min=1, index=2

# Q58. Implement SENTINEL linear search (place the target at the end to avoid boundary check in loop).
#      Example: [10, 20, 30, 40, 50], target=30 → Found at index 2

# Q59. Implement TRANSPOSITION linear search: each time an element is found,
#      move it one position to the LEFT (swap with previous element).
#      Example: [10, 20, 30, 40], search 30 → [10, 30, 20, 40] (30 moved left by 1)

# Q60. Find the element in a list that is closest in value to a given target (not exact match needed).
#      Example: [10, 22, 35, 47, 60], target=38 → 35


# =============================================================================
# SECTION 4 - BINARY SEARCH (Q61-Q85)
# =============================================================================

# Q61. Implement ITERATIVE binary search on a sorted list. Return the index or -1.
#      Example: [1, 3, 5, 7, 9, 11], target=7 → 3

# Q62. Implement RECURSIVE binary search on a sorted list. Return the index or -1.
#      Example: [2, 4, 6, 8, 10], target=6 → 2

# Q63. Count the number of comparisons (steps) made during binary search.
#      Example: [1, 2, 3, 4, 5, 6, 7, 8], target=6 → steps=3

# Q64. Perform binary search only within a specific range [left, right] of the list.
#      Example: [1, 3, 5, 7, 9, 11, 13], search 9 in range [2, 5] → index 4

# Q65. Find the FIRST occurrence of a target in a sorted list that may contain duplicates.
#      Example: [1, 2, 2, 2, 3, 4], target=2 → index 1

# Q66. Find the LAST occurrence of a target in a sorted list that may contain duplicates.
#      Example: [1, 2, 2, 2, 3, 4], target=2 → index 3

# Q67. Count the total occurrences of a target in a sorted array using binary search
#      (use first and last occurrence).
#      Example: [1, 2, 2, 2, 3, 4], target=2 → 3

# Q68. Find the index at which a target should be INSERTED to keep a sorted list sorted.
#      Example: [1, 3, 5, 6], target=4 → insert at index 2

# Q69. First check if the array is sorted, then apply binary search. Print a warning if unsorted.
#      Example: [1, 3, 5, 7], target=5 → sorted, found at index 2
#               [3, 1, 4, 2], target=3 → "Array not sorted, cannot apply binary search"

# Q70. Apply binary search on a list of FLOATS.
#      Example: [1.1, 2.2, 3.3, 4.4, 5.5], target=3.3 → index 2

# Q71. Find the integer square root of a number using binary search (floor of sqrt).
#      Example: n=26 → 5 (since 5²=25 ≤ 26 < 36=6²)

# Q72. Find a PEAK element in an array (element greater than its neighbors).
#      A peak element is not necessarily the global max.
#      Example: [1, 3, 20, 4, 1, 0] → index 2 (value 20)

# Q73. Search for a target in a ROTATED sorted array (no duplicates).
#      Example: [4, 5, 6, 7, 0, 1, 2], target=0 → index 4

# Q74. Find the MINIMUM element in a rotated sorted array.
#      Example: [4, 5, 6, 7, 0, 1, 2] → 0 at index 4

# Q75. Find the missing number in a sorted array of consecutive integers using binary search.
#      Example: [0, 1, 2, 3, 5, 6, 7] → missing = 4

# Q76. Perform binary search on a ROW-WISE and COLUMN-WISE sorted 2D matrix.
#      Example: [[1,3,5],[7,9,11],[13,15,17]], target=9 → (1, 1)

# Q77. Find the FLOOR of a target in a sorted array (largest element ≤ target).
#      Example: [1, 2, 4, 6, 8, 10], target=7 → 6

# Q78. Find the CEILING of a target in a sorted array (smallest element ≥ target).
#      Example: [1, 2, 4, 6, 8, 10], target=5 → 6

# Q79. Find the Kth smallest element concept: sort and return the element at index k-1.
#      Then discuss how binary search on answer space could be applied.
#      Example: [7, 10, 4, 3, 20, 15], k=3 → 7

# Q80. Simulate binary search on an "infinite" sorted array by doubling the search range
#      until the target's range is found, then apply binary search.
#      Example: arr=[1,2,3,4,...,1000], target=500 → found (simulate with a large list)

# Q81. Find a FIXED POINT in a sorted array: index i such that arr[i] == i.
#      Example: [-10, -5, 0, 3, 7] → index 3 (arr[3]=3)

# Q82. Search for a target in a NEARLY SORTED array (each element may be displaced by 1 position).
#      Example: [10, 3, 40, 20, 50, 80, 70], target=40 → index 2

# Q83. Count the number of 1s in a sorted binary array (contains only 0s and 1s) using binary search.
#      Example: [0, 0, 0, 1, 1, 1, 1] → 4 ones

# Q84. Search for a target in a BITONIC array (first increases then decreases).
#      First find the peak, then binary search in both halves.
#      Example: [1, 3, 8, 12, 4, 2], target=12 → index 3

# Q85. Aggressive Cows problem: Given n stalls and c cows, find the largest minimum distance
#      between any two cows using binary search on the answer.
#      Example: stalls=[1, 2, 4, 8, 9], cows=3 → max_min_distance = 3


# =============================================================================
# SECTION 5 - SORTING (Q86-Q120)
# =============================================================================

# Q86. Implement BUBBLE SORT. Sort a list in ascending order.
#      Example: [64, 34, 25, 12, 22, 11, 90] → [11, 12, 22, 25, 34, 64, 90]

# Q87. Implement SELECTION SORT. Find the minimum and place it at the front each pass.
#      Example: [29, 10, 14, 37, 13] → [10, 13, 14, 29, 37]

# Q88. Implement INSERTION SORT. Build the sorted list one element at a time.
#      Example: [12, 11, 13, 5, 6] → [5, 6, 11, 12, 13]

# Q89. Count the total number of SWAPS performed during bubble sort.
#      Example: [4, 3, 2, 1] → sorted=[1,2,3,4], swaps=6

# Q90. Check if an array needs sorting (is it already sorted?) before applying a sort algorithm.
#      Print "Already sorted" or proceed with sort.
#      Example: [1, 2, 3, 4] → "Already sorted"; [3, 1, 2] → sort it

# Q91. Sort a list WITHOUT using the built-in sort() or sorted() — use your own algorithm.
#      Example: [5, 3, 8, 1, 9, 2] → [1, 2, 3, 5, 8, 9]

# Q92. Sort a list of STRINGS alphabetically (case-insensitive).
#      Example: ["Banana", "apple", "Cherry", "date"] → ["apple", "Banana", "Cherry", "date"]

# Q93. Sort a list of strings by their LENGTH (shortest to longest). Use stable sort for ties.
#      Example: ["banana", "fig", "apple", "kiwi"] → ["fig", "kiwi", "apple", "banana"]

# Q94. Sort a list of TUPLES by the second element of each tuple.
#      Example: [(1, 3), (4, 1), (2, 2)] → [(4,1), (2,2), (1,3)]

# Q95. Sort a list of DICTIONARIES by a specific key (e.g., "age").
#      Example: [{"name":"Bob","age":30},{"name":"Alice","age":25}] → Alice first

# Q96. Implement MERGE SORT (divide and conquer). Return the sorted list.
#      Example: [38, 27, 43, 3, 9, 82, 10] → [3, 9, 10, 27, 38, 43, 82]

# Q97. Implement QUICK SORT using the last element as pivot.
#      Example: [10, 80, 30, 90, 40, 50, 70] → [10, 30, 40, 50, 70, 80, 90]

# Q98. Implement COUNTING SORT for a list of non-negative integers.
#      Example: [4, 2, 2, 8, 3, 3, 1] → [1, 2, 2, 3, 3, 4, 8]

# Q99. Implement RADIX SORT concept for non-negative integers (sort by each digit, LSD first).
#      Example: [170, 45, 75, 90, 802, 24, 2, 66] → [2, 24, 45, 66, 75, 90, 170, 802]

# Q100. Sort an array containing only 0s, 1s, and 2s in a single pass (Dutch National Flag algorithm).
#       Example: [2, 0, 2, 1, 1, 0] → [0, 0, 1, 1, 2, 2]

# Q101. Find the Kth LARGEST element using sort().
#       Example: [3, 2, 1, 5, 6, 4], k=2 → 5

# Q102. Find the Kth SMALLEST element using sort().
#       Example: [7, 10, 4, 3, 20, 15], k=3 → 7

# Q103. Sort a NEARLY SORTED array efficiently (each element is at most k positions from sorted).
#       Example: [6, 5, 3, 2, 8, 10, 9], k=3 → [2, 3, 5, 6, 8, 9, 10]

# Q104. Sort a list by ABSOLUTE VALUE (ignoring sign).
#       Example: [-4, 3, -1, 2, -5] → [-1, 2, 3, -4, -5]

# Q105. Sort a list so that all EVEN numbers come first, then ODD numbers.
#       Maintain relative order within each group.
#       Example: [1, 2, 3, 4, 5, 6] → [2, 4, 6, 1, 3, 5]

# Q106. Rearrange an array so that POSITIVE and NEGATIVE numbers alternate.
#       (Assume equal counts of positives and negatives.)
#       Example: [-1, 2, -3, 4, -5, 6] → [2, -1, 4, -3, 6, -5]

# Q107. Sort an array by FREQUENCY of elements (most frequent first, ties broken by value).
#       Example: [4, 5, 6, 5, 4, 3, 4] → [4, 4, 4, 5, 5, 6, 3]

# Q108. Find the MEDIAN of a list after sorting it.
#       Example: [3, 1, 4, 1, 5] → sorted=[1,1,3,4,5], median=3
#                [1, 2, 3, 4] → median = (2+3)/2 = 2.5

# Q109. Check if two lists are equal when both are sorted (contain same elements).
#       Example: [3, 1, 2] and [2, 3, 1] → True; [1, 2, 3] and [1, 2, 4] → False

# Q110. Sort all CHARACTERS of a string alphabetically.
#       Example: "programming" → "aggimmnoprr"

# Q111. Implement CYCLIC SORT — works for arrays containing numbers from 1 to n.
#       Place each number at its correct index (value - 1).
#       Example: [3, 1, 5, 4, 2] → [1, 2, 3, 4, 5]

# Q112. Sort a list of people by MULTIPLE CRITERIA: first by age (ascending),
#       then by name (alphabetically) for ties.
#       Example: [("Alice",30),("Bob",25),("Charlie",25)] → [("Bob",25),("Charlie",25),("Alice",30)]

# Q113. Sort a list IN-PLACE and also create a NEW sorted list without changing the original.
#       Demonstrate the difference between list.sort() (in-place) and sorted() (new list).
#       Example: a=[3,1,2] → a.sort() modifies a; sorted(a) leaves a unchanged

# Q114. # CONCEPT COMMENT (no code required):
#       # STABLE vs UNSTABLE SORT:
#       # - Stable sort: preserves the relative order of equal elements.
#       #   Examples: Merge Sort, Insertion Sort, Python's built-in sort (Timsort).
#       # - Unstable sort: does NOT guarantee order of equal elements.
#       #   Examples: Quick Sort, Heap Sort, Selection Sort.
#       # Python's sort() and sorted() are stable (Timsort).

# Q115. # CONCEPT COMMENT (no code required):
#       # TIM SORT:
#       # - Timsort is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort.
#       # - Used in Python's built-in sort() and Java's Arrays.sort() for objects.
#       # - It divides the array into small 'runs' and sorts them using Insertion Sort,
#       #   then merges the runs using Merge Sort.
#       # - Best case: O(n), Average/Worst case: O(n log n), Space: O(n).
#       # - It is stable and performs exceptionally well on real-world data.

# Q116. Sort a list of strings by their LAST CHARACTER.
#       Example: ["banana", "apple", "cherry"] → ["apple", "banana", "cherry"] (a, e, y → sorted by last char)

# Q117. Sort a list of integers in DESCENDING order using sorted() with reverse=True.
#       Example: [3, 1, 4, 1, 5, 9] → [9, 5, 4, 3, 1, 1]

# Q118. Given a list of words, sort them so that PALINDROMES come first, then others.
#       Example: ["racecar", "hello", "madam", "world"] → ["racecar", "madam", "hello", "world"]

# Q119. Sort a list of (x, y) COORDINATE tuples by their distance from the origin (0, 0).
#       Example: [(3,4),(1,1),(0,5)] → [(1,1),(3,4),(0,5)] (distances: √2, 5, 5)

# Q120. Implement SHELL SORT (generalization of insertion sort using gap sequence).
#       Example: [12, 34, 54, 2, 3] → [2, 3, 12, 34, 54]


# =============================================================================
# SECTION 6 - MIXED / ADVANCED (Q121-Q150)
# =============================================================================

# Q121. TWO POINTER — Pair with target sum (sorted array):
#       Use left and right pointers to find a pair that sums to the target.
#       Example: [1, 2, 3, 4, 6], target=6 → (2, 4)

# Q122. TWO POINTER — Remove duplicates from a SORTED array in-place.
#       Return the new length (modify the list so unique elements are at the front).
#       Example: [1, 1, 2, 2, 3, 4, 4] → length=4, list becomes [1, 2, 3, 4, ...]

# Q123. TWO POINTER — Move all zeros to the end while maintaining order of non-zero elements.
#       Do it in-place using two pointers.
#       Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

# Q124. SLIDING WINDOW — Maximum sum of a subarray of exactly size k.
#       Example: [2, 1, 5, 1, 3, 2], k=3 → 9 (subarray [5,1,3])

# Q125. SLIDING WINDOW — Find the length of the smallest subarray with sum >= S.
#       Example: [2, 3, 1, 2, 4, 3], S=7 → 2 (subarray [4,3])

# Q126. Build a PREFIX SUM array where prefix[i] = sum of arr[0..i].
#       Then answer range sum queries in O(1).
#       Example: arr=[1,2,3,4,5] → prefix=[1,3,6,10,15]; sum(1,3)=prefix[3]-prefix[0]=9

# Q127. Find a CONTIGUOUS SUBARRAY with a given sum (positive integers).
#       Return the start and end indices.
#       Example: [1, 4, 20, 3, 10, 5], target=33 → subarray [20,3,10] indices (2, 4)

# Q128. KADANE'S ALGORITHM — Find the maximum sum of any contiguous subarray.
#       Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4,-1,2,1])

# Q129. Find the MINIMUM sum of any contiguous subarray.
#       Example: [3, -4, 2, -3, -1, 7, -5] → -6 (subarray [-4,2,-3,-1])

# Q130. PRODUCT OF ARRAY EXCEPT SELF — For each index i, compute product of all elements except arr[i].
#       Do not use division.
#       Example: [1, 2, 3, 4] → [24, 12, 8, 6]

# Q131. Find ALL TRIPLETS in an array that sum to zero.
#       Example: [-1, 0, 1, 2, -1, -4] → [(-1,-1,2), (-1,0,1)]

# Q132. Find the LONGEST CONSECUTIVE SEQUENCE in an unsorted array.
#       Example: [100, 4, 200, 1, 3, 2] → longest sequence [1,2,3,4], length=4

# Q133. Find the DUPLICATE number in an array of n+1 integers where each integer is in [1, n].
#       (Only one duplicate exists.)
#       Example: [1, 3, 4, 2, 2] → 2

# Q134. Find the SINGLE NON-REPEATING element in an array where every other element appears twice.
#       Use XOR for O(n) time and O(1) space.
#       Example: [4, 1, 2, 1, 2] → 4

# Q135. Find the MAJORITY ELEMENT — element that appears more than n/2 times.
#       Use Boyer-Moore Voting Algorithm.
#       Example: [2, 2, 1, 1, 1, 2, 2] → 2

# Q136. STOCK BUY SELL — Find the maximum profit from a single buy and sell transaction.
#       Example: [7, 1, 5, 3, 6, 4] → profit=5 (buy at 1, sell at 6)

# Q137. TRAPPING RAIN WATER — Given heights of walls, compute total water trapped.
#       Example: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] → 6 units

# Q138. NEXT GREATER ELEMENT — For each element, find the next greater element to its right.
#       Use a stack. Return -1 if none exists.
#       Example: [4, 5, 2, 25] → [5, 25, 25, -1]

# Q139. PREVIOUS SMALLER ELEMENT — For each element, find the nearest smaller element to its left.
#       Use a stack. Return -1 if none exists.
#       Example: [3, 8, 5, 2, 25] → [-1, 3, 3, -1, 2]

# Q140. SPIRAL ORDER MATRIX TRAVERSAL — Print all elements of a 2D matrix in spiral order.
#       Example: [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5]

# Q141. ROTATE MATRIX 90 DEGREES CLOCKWISE in-place (for n×n matrix).
#       Example: [[1,2,3],[4,5,6],[7,8,9]] → [[7,4,1],[8,5,2],[9,6,3]]

# Q142. TRANSPOSE a matrix (swap rows and columns).
#       Example: [[1,2,3],[4,5,6],[7,8,9]] → [[1,4,7],[2,5,8],[3,6,9]]

# Q143. Find the DIAGONAL SUM of a square matrix (sum of both main and anti-diagonal,
#       subtract middle element if n is odd to avoid double counting).
#       Example: [[1,2,3],[4,5,6],[7,8,9]] → 1+5+9 + 3+5+7 - 5 = 25

# Q144. Find the SADDLE POINT in a matrix — element that is minimum in its row
#       and maximum in its column.
#       Example: [[1,2,3],[4,5,6],[7,8,9]] → saddle point = 7 at (2,0)

# Q145. Search in a ROW-WISE and COLUMN-WISE sorted matrix efficiently (start from top-right corner).
#       Example: [[10,20,30],[15,25,35],[27,29,37]], target=29 → (2, 1)

# Q146. MERGE OVERLAPPING INTERVALS — Given a list of intervals, merge all overlapping ones.
#       Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

# Q147. MINIMUM JUMPS TO REACH END — Find the minimum number of jumps to reach the last index.
#       arr[i] = max steps you can jump forward from index i.
#       Example: [2, 3, 1, 1, 4] → 2 jumps (0→1→4)

# Q148. COUNT INVERSIONS — Count pairs (i, j) where i < j but arr[i] > arr[j].
#       Use a modified merge sort.
#       Example: [2, 4, 1, 3, 5] → 3 inversions: (2,1),(4,1),(4,3)

# Q149. FIND MEDIAN OF TWO SORTED ARRAYS of total combined size n+m.
#       Example: [1, 3] and [2] → median = 2.0
#                [1, 2] and [3, 4] → median = 2.5

# Q150. MAXIMUM PRODUCT SUBARRAY — Find the contiguous subarray with the largest product.
#       Track both max and min at each step (negative × negative = positive).
#       Example: [2, 3, -2, 4] → 6 (subarray [2,3])
#                [-2, 0, -1] → 0


# =============================================================================
# QUICK REFERENCE CHEAT SHEET
# =============================================================================
#
# ── LIST BASICS ──────────────────────────────────────────────────────────────
#  Create          : arr = [1, 2, 3]  |  arr = list(range(1, 6))
#  Index           : arr[0]  arr[-1]  (negative = from end)
#  Slice           : arr[1:4]  arr[::2]  arr[::-1]  (reverse)
#  Length          : len(arr)
#  Append          : arr.append(x)
#  Insert          : arr.insert(index, x)
#  Remove by value : arr.remove(x)       # removes first occurrence
#  Remove by index : arr.pop(index)      # default pops last
#  Count           : arr.count(x)
#  Find index      : arr.index(x)        # raises ValueError if not found
#  In check        : x in arr            # O(n)
#  Sort in-place   : arr.sort()          # arr.sort(reverse=True) for desc
#  New sorted copy : sorted(arr)
#  Reverse in-place: arr.reverse()
#  Copy            : arr.copy()  or  arr[:]
#  Concatenate     : arr1 + arr2
#  Repeat          : arr * n
#  List comp       : [x**2 for x in range(10) if x % 2 == 0]
#  2D list         : matrix = [[0]*cols for _ in range(rows)]
#
# ── SEARCHING ────────────────────────────────────────────────────────────────
#  Linear Search   : O(n)  — works on unsorted arrays
#  Binary Search   : O(log n) — requires SORTED array
#  bisect module   : bisect.bisect_left(arr, x)   # insert position (left)
#                    bisect.bisect_right(arr, x)  # insert position (right)
#                    bisect.insort(arr, x)         # insert in sorted order
#
# ── SORTING ALGORITHMS COMPLEXITY ────────────────────────────────────────────
#  Algorithm       Best        Average     Worst       Space   Stable?
#  Bubble Sort   : O(n)        O(n²)       O(n²)       O(1)    Yes
#  Selection Sort: O(n²)       O(n²)       O(n²)       O(1)    No
#  Insertion Sort: O(n)        O(n²)       O(n²)       O(1)    Yes
#  Merge Sort    : O(n log n)  O(n log n)  O(n log n)  O(n)    Yes
#  Quick Sort    : O(n log n)  O(n log n)  O(n²)       O(log n) No
#  Counting Sort : O(n+k)      O(n+k)      O(n+k)      O(k)    Yes
#  Radix Sort    : O(nk)       O(nk)       O(nk)       O(n+k)  Yes
#  Tim Sort      : O(n)        O(n log n)  O(n log n)  O(n)    Yes
#  Shell Sort    : O(n log n)  O(n log²n)  O(n²)       O(1)    No
#  Cyclic Sort   : O(n)        O(n)        O(n)        O(1)    No
#
# ── KEY TECHNIQUES ───────────────────────────────────────────────────────────
#  Two Pointers    : Use left/right pointers moving toward each other.
#                    Best for sorted arrays. O(n) time, O(1) space.
#
#  Sliding Window  : Maintain a window [l, r] expanding/shrinking.
#                    Best for subarray/substring problems. O(n) time.
#
#  Prefix Sum      : prefix[i] = sum(arr[0..i])
#                    Range sum query: prefix[r] - prefix[l-1]  →  O(1)
#
#  Kadane's Algo   : max_sum = curr_sum = arr[0]
#                    for x in arr[1:]: curr_sum = max(x, curr_sum+x)
#                                      max_sum  = max(max_sum, curr_sum)
#
#  XOR Trick       : a ^ a = 0,  a ^ 0 = a  →  find single non-repeat
#
#  Boyer-Moore     : Majority element voting — cancel out different pairs.
#
#  Dutch Nat. Flag : Three-way partition with lo, mid, hi pointers.
#
#  Binary Search   : lo, hi = 0, len(arr)-1
#  (template)        while lo <= hi:
#                        mid = (lo + hi) // 2
#                        if arr[mid] == target: return mid
#                        elif arr[mid] < target: lo = mid + 1
#                        else: hi = mid - 1
#                    return -1
#
# ── USEFUL BUILT-INS ─────────────────────────────────────────────────────────
#  sum(arr)             max(arr)            min(arr)
#  enumerate(arr)       zip(a, b)           reversed(arr)
#  map(fn, arr)         filter(fn, arr)     reduce(fn, arr)  # from functools
#  any(arr)             all(arr)            abs(x)
#  sorted(arr, key=fn)  arr.sort(key=fn)
#
# ── COMMON PATTERNS ──────────────────────────────────────────────────────────
#  Flatten 2D      : [x for row in matrix for x in row]
#  Remove dups     : list(dict.fromkeys(arr))  # preserves order
#  Frequency dict  : from collections import Counter; Counter(arr)
#  Rotate left k   : arr[k:] + arr[:k]
#  Rotate right k  : arr[-k:] + arr[:-k]
#  Swap in-place   : arr[i], arr[j] = arr[j], arr[i]
#  2D matrix size  : rows=len(m), cols=len(m[0])
#
# =============================================================================
# END OF CHEAT SHEET
# =============================================================================
