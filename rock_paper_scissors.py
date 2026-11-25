import random

VALID_CHOICES = ["rock", "paper", "scissor"]
def game_explain() -> None:
    """Display the game rules and scoring."""
    print(
        "\n=== Rock Paper Scissor ===\n"
        "Choose how many rounds you want to play.\n"
        "Each round, choose rock, paper, or scissor to compete against the computer.\n"
        "Rock beats scissor, scissor beats paper, and paper beats rock.\n"
        "Matching choices result in a tie. Ties count toward the chosen rounds.\n"
        "Each round you win earns 1 point.\n"
        "The overall winner is determined by the number of rounds won.\n"
        "Equal win counts result in a draw.\n"
        "=== Good Luck!!! ===\n"
    )


def get_rounds() -> int:
    """Return a positive number of rounds entered by the player."""
    while True:
        try:
            rounds = int(input("Enter the number of rounds: "))
            if rounds <= 0:
                raise ValueError("Round must be an integer greater than 0.")
            return rounds
        except ValueError:
            print("Please enter a whole number greater than 0")

def user_choice() -> str:
    """Return a valid rock, paper, or scissors choice or error message"""
    while True:
        user = input("Enter your choice, Rock, Paper, or Scissor: ").lower().strip()
        if user in VALID_CHOICES:
            return user
        print("Invalid choice. Please enter rock, paper, or scissor.")

def computer_choice() -> str:
    """A randomly generated choice from rock, peper, scissors"""
    return random.choice(VALID_CHOICES)

def decide_win_lose_each_round( user: str,  computer: str) -> str:
    """
    compares the user and computer's choice and decides if the user won, lost or tie
    param user: user's choice
    param computer: computer's choice
    return: win or lost or tie (string)
    """
    return "tie" if (
        (computer == user)
    ) else "win" if (
        (user == "rock" and computer == "scissor") or
        (user == "paper" and computer == "rock") or
        (user == "scissor" and computer == "paper")
    ) else "lose"

def main():
    game_explain()
    rounds = get_rounds()
    user_score = 0
    computer_score = 0
    for i in range(rounds):
        user = user_choice()
        computer = computer_choice()
        result = decide_win_lose_each_round(user, computer)
        user_score += 1 if result == "win" else 0
        computer_score += 1 if result == "lose" else 0
        print(f"\tYou chose {user} and your opponent chose {computer}.\n\tYour current score: {user_score} and your opponent's current score: {computer_score}")

    print("Congratulations!!! You won"
        if user_score > computer_score
        else "You lost! Please Try again"
        if user_score < computer_score
        else "It's a draw! Better Luck next time!")
    print("You total score is ", user_score)


if __name__ == "__main__":
    main()
