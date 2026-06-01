# Example 1: Basic for loop
print("1. Basic Loop:")
for i in range(5):
    print("Value of i:", i)


# Example 2: Loop through a list
print("\n2. Loop through a list:")
items = ["apple", "banana", "mango"]
for item in items:
    print("Item:", item)


# Example 3: Loop through a string
print("\n3. Loop through a string:")
for ch in "Python":
    print("Character:", ch)


# Example 4: Using break
print("\n4. Using break:")
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)


# Example 5: Using continue
print("\n5. Using continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)


# Example 6: Nested for loop
print("\n6. Nested loop (i, j pairs):")
for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)


# Example 7: Pattern printing
print("\n7. Pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# Example 8: for loop with else
print("\n8. For-Else:")
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")  