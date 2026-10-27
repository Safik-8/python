import random
from game_config import DIFFICULTIES

def get_valid_guess(low, high):
    # Keep asking until the player enters a valid number in range.
    # A bad input does NOT cost the player a guess.
    while True:
        raw = input(f"  Guess ({low}-{high}): ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("  That's not a whole number. Try again.")
            continue
        if not low <= guess <= high:
            print(f"  Out of range. Pick between {low} and {high}.")
            continue
        return guess

def proximity_hint(guess, secret, span):
    # Return a 'warmth' hint based on how close the guess is.
    distance = abs(guess - secret)
    if distance == 0:
        return "correct"
    ratio = distance / span
    if ratio <= 0.05:  return "burning hot"
    elif ratio <= 0.10: return "hot"
    elif ratio <= 0.20: return "warm"
    elif ratio <= 0.35: return "cool"
    return "cold"

def play_round(difficulty):
    config = DIFFICULTIES[difficulty]
    low, high = config["low"], config["high"]
    max_guesses = config["max_guesses"]
    span = high - low

    secret = random.randint(low, high)
    print(f"\n  I'm thinking of a number between {low} and {high}.")
    print(f"  You have {max_guesses} guesses. Good luck!\n")

    for attempt in range(1, max_guesses + 1):
        guess = get_valid_guess(low, high)

        if guess == secret:
            print(f"  Correct! You won in {attempt} guess(es)!")
            return attempt         # return guesses used (a win)

        # Give directional + proximity feedback
        direction = "Too high!" if guess > secret else "Too low!"
        warmth    = proximity_hint(guess, secret, span)
        remaining = max_guesses - attempt
        print(f"  {direction} ({warmth}) - {remaining} guess(es) left\n")

    print(f"  Out of guesses! The number was {secret}.")
    return None                    # None means the player lost
