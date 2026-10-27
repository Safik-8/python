# Difficulty configuration - data-driven design.
# Adding a new level is just one more dictionary entry.
DIFFICULTIES = {
    "easy":   {"low": 1, "high": 50,  "max_guesses": 10, "multiplier": 1},
    "medium": {"low": 1, "high": 100, "max_guesses": 7,  "multiplier": 2},
    "hard":   {"low": 1, "high": 200, "max_guesses": 5,  "multiplier": 3},
}

import random

# --- The random module: core functions for games --------
print(random.randint(1, 100))      # random integer 1-100 (both inclusive)
print(random.random())             # random float 0.0 - 1.0
print(random.choice(["a","b","c"])) # random pick from a sequence
print(random.shuffle([1,2,3,4]))   # shuffles a list in place

# --- Picking the secret number for a chosen difficulty ---
def pick_secret(difficulty):
    config = DIFFICULTIES[difficulty]
    secret = random.randint(config["low"], config["high"])
    return secret, config

secret, config = pick_secret("medium")
print(f"Secret is between {config['low']} and {config['high']}")
# (In the real game we never print the secret - that's the puzzle!)

# --- random.seed: reproducible randomness (useful for testing) ---
random.seed(42)                    # fixes the sequence
print(random.randint(1, 100))      # same result every run with this seed
random.seed()                      # reset to truly random again
