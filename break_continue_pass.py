#BREAK

# The break statement is used to exit a loop prematurely.
# Example:
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0, 1, 2, 3, 4
    
    
    
#CONTINUE

# The continue statement skips the rest of the code in the current iteration and moves to the next iteration.
# Example:

for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0, 1, 3, 4
    
    
#PASS

# The pass statement is a placeholder that does nothing. It is used when syntax requires a statement but no action is needed.
# Example:

for i in range(5):
    if i == 3:
        pass  # Do nothing
    print(i)  # Output: 0, 1, 2, 3, 
