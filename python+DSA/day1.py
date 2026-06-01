# ---------------------------------------------------------------------QUIZ APPLICATION-----------------------------------------------------------------------------------------------------------------------
def result(score,total):
    percentage = (score/total) * 100
    
    print("Your score:"+ str(score) + "/" + str(total))
    print("Your percentage:"+ str(percentage) + "%")
    
    if percentage >= 60:
        print(" You passed")
    else:
        print(" Better luck next time")
        print("Please try again.")
        
        
def quiz():
    score = 0
    total = 10
    
    
    questions = ["Which keyword is used to define a function in Python?\n(a) func\n(b) define\n(c) def\n(d) function",
                 "Which data type is used to store whole numbers in Python?\n(a) bool\n(b) float\n(c) str\n(d) int",
                 "What is the output of 5 + 3?\n(a) 5\n(b) 8\n(c) 10\n(d) 12",
                 "Which loop is commonly used to iterate through a list?\n(a) for loop\n(b) while loop\n(c) do-while loop\n(d) foreach loop",
                 "Which function is used to take input from the user in Python?\n(a) scanf()\n(b) input()\n(c) read()\n(d) get()",
                 "Which symbol is used for comments in Python?\n(a) #\n(b) //\n(c) /* */\n(d) --",
                 "Which operator is used to check equality?\n(a) ===\n(b) =\n(c) ==\n(d) !==",
                 "What does HTML stand for?\n(a) HighText Markup Language\n(b) HighText Machine Language\n(c) HyperText Markup Leveler\n(d) HyperText Markup Language",
                 "Which of the following is a Python collection data type?\n(a) list\n(b) char\n(c) double\n(d) pointer",
                 "Which language is primarily used for web page structure?\n(a) JavaScript\n(b) CSS\n(c) HTML\n(d) Python"] 

    answers = ['c','d','b','a','b','a','c','d','a','c'] 


    for i in range(len(questions)):
        print(questions[i])
        user_answer = input("Your answer: ")
        if user_answer == answers[i]:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    result(score,total)
    play_again()

def play_again():
    
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == 'yes':
        quiz()
    else:
        print("Thank you for playing!")
    

quiz()