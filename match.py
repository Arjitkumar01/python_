

while True:
    print("\n========== MAIN MENU ==========")
    print("1. Calculator")
    print("2. Number Type Checker")
    print("3. Day Type Checker")
    print("4. Grade System")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:

        
        case "1":
            print("\n--- Calculator ---")
            op = input("Enter operation (+, -, *, /): ")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            match op:
                case "+":
                    print("Result:", a + b)
                case "-":
                    print("Result:", a - b)
                case "*":
                    print("Result:", a * b)
                case "/":
                    match b:
                        case 0:
                            print("Error: Division by zero!")
                        case _:
                            print("Result:", a / b)
                case _:
                    print("Invalid operation!")

        
        case "2":
            print("\n--- Number Checker ---")
            num = int(input("Enter a number: "))

            match num:
                case 0:
                    print("Number is Zero")
                case _ if num > 0:
                    print("Positive Number")
                case _ if num < 0:
                    print("Negative Number")

        
        case "3":
            print("\n--- Day Checker ---")
            day = input("Enter a day: ").lower()

            match day:
                case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
                    print("It's a Weekday")
                case "saturday" | "sunday":
                    print("It's a Weekend")
                case _:
                    print("Invalid day!")

        
        case "4":
            print("\n--- Grade System ---")
            marks = int(input("Enter your marks: "))

            match marks:
                case _ if marks >= 90:
                    print("Grade: A+")
                case _ if marks >= 75:
                    print("Grade: A")
                case _ if marks >= 60:
                    print("Grade: B")
                case _ if marks >= 50:
                    print("Grade: C")
                case _:
                    print("Grade: Fail")

        
        case "5":
            print("Exiting program... 👋")
            break

        
        case _:
            print("Invalid choice! Try again.")