def get_range_for_difficulty(difficulty: str):
    # FIX: Hard mode now has a larger range so it is actually harder

    if difficulty == "Easy":
        return 1, 20

    if difficulty == "Normal":
        return 1, 100

    if difficulty == "Hard":
        return 1, 200

    return 1, 100


def parse_guess(raw: str):

    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    # FIX: Corrected hint direction after using Codex to review logic
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

def update_score(current_score: int, outcome: str, attempt_number: int):

    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)

        if points < 10:
            points = 10

        return current_score + points

    if outcome in ["Too High", "Too Low"]:
        return current_score - 5  # FIX: remove reward bug

    return current_score