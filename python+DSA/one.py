# # Word Guessing Game

# def word_guessing_game():
#     word_to_guess = "python"
#     attempts = 5
    

#     print("Welcome to the Word Guessing Game!")
#     print(f"You have {attempts} attempts to guess the word.")
    

#     while attempts > 0:
#         print("Hint: It's a popular programming language.")
#         guess = input("Enter your guess: ").lower()

#         if guess == word_to_guess:
#             print("Congratulations! You've guessed the word correctly!")
#             play_again()
#             break
#         else:
#             attempts -= 1
#             print(f"Wrong guess! You have {attempts} attempts left.")
        
        
#     if attempts == 0:
#         print(f"Game over! The word was: {word_to_guess}")
#         play_again()


# def play_again():
#     choice = input("Play again? (yes/no): ").lower()

#     if choice == "yes":
#         word_guessing_game()
#     elif choice == "no":
#         print("Thank you for playing!")
#     else:
#         print("Invalid ")
#         play_again()   # recursion
# #--------------------------------------------------------------------------------------        

# word_guessing_game()


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         for i in range(len(nums)):
#             if val in nums:
#                 nums.remove(val)

#         print(nums)

# l1=Solution()
# l1.removeElement([12,2,5,3,44,6,3,4,5,3],3)



