import json
from pathlib import Path
from datetime import datetime

LEADERBOARD_FILE = Path("leaderboard.json")
MAX_ENTRIES = 10

def load_leaderboard():
    # Load the saved high scores, or return an empty list.
    if not LEADERBOARD_FILE.exists():
        return []
    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []                  # corrupted file -> start fresh

def save_score(name, score, difficulty):
    # Add a score and keep only the top 10.
    board = load_leaderboard()
    board.append({
        "name":       name,
        "score":      score,
        "difficulty": difficulty,
        "date":       datetime.now().strftime("%Y-%m-%d"),
    })
    # Sort by score descending, keep the best MAX_ENTRIES
    board.sort(key=lambda entry: entry["score"], reverse=True)
    board = board[:MAX_ENTRIES]

    try:
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(board, f, indent=2)
    except OSError as e:
        print(f"  Could not save score: {e}")
    return board

def is_high_score(score):
    # Is this score good enough for the leaderboard?
    board = load_leaderboard()
    if len(board) < MAX_ENTRIES:
        return True
    return score > board[-1]["score"]    # beats the lowest entry

def show_leaderboard():
    board = load_leaderboard()
    if not board:
        print("  No scores yet. Be the first!")
        return
    print("\n  ===== HIGH SCORES =====")
    print(f"  {'Rank':<5}{'Name':<14}{'Score':<8}{'Level':<8}{'Date'}")
    print("  " + "-" * 45)
    for rank, entry in enumerate(board, 1):
        print(f"  {rank:<5}{entry['name']:<14}{entry['score']:<8}"
              f"{entry['difficulty']:<8}{entry['date']}")
