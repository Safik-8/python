import random
from game_config import DIFFICULTIES
from scoring import calculate_score
from leaderboard import (save_score, is_high_score,
                         show_leaderboard, load_leaderboard)

def choose_difficulty():
    # Ask until a valid difficulty is chosen.
    while True:
        choice = input("  Difficulty [easy/medium/hard]: ").strip().lower()
        if choice in DIFFICULTIES:
            return choice
        print("  Please type easy, medium, or hard.")

def play_round(difficulty):
    config = DIFFICULTIES[difficulty]
    low, high = config["low"], config["high"]
    max_guesses = config["max_guesses"]
    span      = high - low
    secret    = random.randint(low, high)

    print(f"\n  Number between {low} and {high}. "
          f"You have {max_guesses} guesses!\n")

    for attempt in range(1, max_guesses + 1):
        # Validate input without costing a guess
        while True:
            raw = input(f"  Guess #{attempt}: ").strip()
            try:
                guess = int(raw)
                if low <= guess <= high:
                    break
                print(f"  Out of range ({low}-{high}).")
            except ValueError:
                print("  Enter a whole number.")

        if guess == secret:
            return attempt         # win: return guesses used

        direction = "Too high" if guess > secret else "Too low"
        distance  = abs(guess - secret)
        warmth    = ("hot" if distance / span <= 0.1
                     else "warm" if distance / span <= 0.25 else "cold")
        print(f"  {direction}! ({warmth}) "
              f"{max_guesses - attempt} left\n")

    print(f"  Out of guesses! It was {secret}.")
    return None                    # loss

def main():
    print("====== NUMBER GUESSING GAME ======")
    show_leaderboard()

    while True:
        difficulty = choose_difficulty()
        guesses    = play_round(difficulty)

        if guesses is not None:         # the player won
            score = calculate_score(guesses, DIFFICULTIES[difficulty])
            print(f"  You scored {score} points!")

            if is_high_score(score):
                print("  NEW HIGH SCORE!")
                name = input("  Enter your name: ").strip() or "Anonymous"
                save_score(name[:12], score, difficulty)
                show_leaderboard()

        again = input("\n  Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("  Thanks for playing!")
            break

if __name__ == "__main__":
    main()
