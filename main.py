import random

def get_choice(value):
    """
    Maps the numeric input to its corresponding choice in the game.
    """
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    return choices.get(value, None)

def determine_winner(machine_choice, user_choice):
    """
    Determines the winner based on the rules of Rock-Paper-Scissors.
    Returns 'draw', 'win', or 'lose'.
    """
    if machine_choice == user_choice:
        return "draw"
    elif (machine_choice == "rock" and user_choice == "paper") or \
         (machine_choice == "paper" and user_choice == "scissors") or \
         (machine_choice == "scissors" and user_choice == "rock"):
        return "win"
    else:
        return "lose"

while True:
    print("------------------------------------------")
    print("1 - rock\n2 - paper\n3 - scissors\n4 - exit game")
    user_input = input("Enter your choice: ")

    # Exit condition
    if user_input == "4":
        print("Exiting the game. Goodbye!")
        break

    # Validate user input
    if not user_input.isdigit() or int(user_input) not in [1, 2, 3]:
        print("Invalid input. Please enter a number between 1 and 3.")
        continue

    user_choice = get_choice(int(user_input))
    machine_choice = get_choice(random.randint(1, 3))

    print(f"\nMachine chose: {machine_choice}")
    print(f"You chose: {user_choice}")

    # Determine and display the result
    result = determine_winner(machine_choice, user_choice)
    if result == "draw":
        print("Result: It's a draw!")
    elif result == "win":
        print("Result: You win!!")
    else:
        print("Result: You lose!!")
