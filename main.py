import random

# -----------------------------
# Number Guessing Game
# -----------------------------
def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n" + "=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("=" * 40)

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess > secret_number:
                print("Go Lower")

            elif guess < secret_number:
                print("Go Higher")

            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")


# -----------------------------
# Quiz Game
# -----------------------------
def quiz_game():
    print("\n" + "=" * 40)
    print("Welcome to Quiz Game!")
    print("=" * 40)

    score = 0

    questions = [
        "What does CPU stand for?",
        "What does RAM stand for?",
        "Which language is mainly used in Data Science?"
    ]

    options = [
        [
            "A. Central Processing Unit",
            "B. Computer Processing Unit",
            "C. Central Program Unit",
            "D. Control Processing Unit"
        ],
        [
            "A. Random Access Memory",
            "B. Read Access Memory",
            "C. Random Active Memory",
            "D. Read Active Memory"
        ],
        [
            "A. HTML",
            "B. CSS",
            "C. Python",
            "D. SQL"
        ]
    ]

    answers = ["A", "A", "C"]

    for i in range(len(questions)):
        print(f"\nQuestion {i+1}")
        print(questions[i])

        for option in options[i]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {answers[i]}")

    print(f"\nYour Final Score: {score}/{len(questions)}")

    # -----------------------------
# Dice Rolling Game
# -----------------------------
def dice_rolling_game():
    print("\n" + "=" * 40)
    print("Welcome to Dice Rolling Game!")
    print("=" * 40)

    while True:
        print("\n1. Roll the Dice")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = random.randint(1, 6)
            print(f"🎲 You rolled: {number}")

        elif choice == "2":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Please enter 1 or 2.")


# -----------------------------
# Rock Paper Scissors Game
# -----------------------------
def rock_paper_scissors():
    print("\n" + "=" * 40)
    print("Welcome to Rock Paper Scissors!")
    print("=" * 40)

    items = ["Rock", "Paper", "Scissor"]

    while True:

        user_choice = input("\nEnter Rock, Paper, Scissor or Exit: ").capitalize()

        if user_choice == "Exit":
            print("Returning to Main Menu...")
            break

        if user_choice not in items:
            print("Invalid Choice!")
            continue

        comp_choice = random.choice(items)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            print("🤝 Match Tie!")

        elif user_choice == "Rock":
            if comp_choice == "Paper":
                print("Paper covers Rock. Computer Wins!")
            else:
                print("Rock breaks Scissor. You Win!")

        elif user_choice == "Paper":
            if comp_choice == "Rock":
                print("Paper covers Rock. You Win!")
            else:
                print("Scissor cuts Paper. Computer Wins!")

        elif user_choice == "Scissor":
            if comp_choice == "Paper":
                print("Scissor cuts Paper. You Win!")
            else:
                print("Rock breaks Scissor. Computer Wins!")

# =============================
# Main Program
# =============================

while True:

    print("\n" + "=" * 45)
    print("         PYTHON GAME HUB")
    print("=" * 45)
    print("1. Number Guessing Game")
    print("2. Quiz Game")
    print("3. Dice Rolling Game")
    print("4. Rock Paper Scissors")
    print("5. Exit")
    print("=" * 45)

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        number_guessing_game()

    elif choice == "2":
        quiz_game()

    elif choice == "3":
        dice_rolling_game()

    elif choice == "4":
        rock_paper_scissors()

    elif choice == "5":
        print("\nThank you for playing Python Game Hub!")
        print("Goodbye 👋")
        break

    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 5.")                