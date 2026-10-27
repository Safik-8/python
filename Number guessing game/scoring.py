def calculate_score(guesses_used, config):
    # Reward fewer guesses and harder difficulty.
    max_guesses = config["max_guesses"]
    multiplier = config["multiplier"]

    # Base: start at 1000, lose points for each guess used
    base = 1000 - (guesses_used - 1) * (800 // max_guesses)
    base = max(base, 100)          # never below 100 for a win

    return base * multiplier

# Examples:
# Easy,   won in 1 guess : (1000) * 1       = 1000
# Medium, won in 4 guesses: (1000 - 3*114) * 2  ~= 1316
# Hard,   won in 2 guesses: (1000 - 1*160) * 3  = 2520
