import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]

    for round_num in range(1, 4):
        print(f"\nRound {round_num}/3")
        my_move = random.choice(options)
        your_move = input("Choose one (rock, paper, scissors): ").strip().lower()

        # If input invalid, notify and skip to next round
        if your_move not in options:
            print("Invalid choice! Please pick rock, paper, or scissors.")
            continue

        # Tie
        if your_move == my_move:
            print(f"It's a tie! We both chose {my_move}.")
        # Player wins
        elif (
            (your_move == "rock"     and my_move == "scissors") or
            (your_move == "paper"    and my_move == "rock")     or
            (your_move == "scissors" and my_move == "paper")
        ):
            print(f"You win! {your_move.capitalize()} beats {my_move}.")
        # Computer wins
        else:
            print(f"You lose! {my_move.capitalize()} beats {your_move}.")

    print("\nGame over! Thanks for playing.")

if __name__ == "__main__":
    rock_paper_scissors()
