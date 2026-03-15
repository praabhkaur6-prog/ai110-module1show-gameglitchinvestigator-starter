from logic_utils import check_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# -------- BONUS EDGE CASE TESTS --------

from logic_utils import parse_guess


def test_parse_guess_invalid_string():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None


def test_parse_guess_empty_input():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None


def test_parse_guess_decimal_input():
    ok, value, err = parse_guess("42.7")
    assert ok is True
    assert value == 42