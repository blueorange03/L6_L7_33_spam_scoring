"""Line-coverage suite for the spam scoring application."""

from spam_scoring import classify, filter_inbox, inbox_status, score_message


def test_scores_spam_signals_and_link_ranges():
    assert score_message("FREE! winner, ALERT", False, 4) == 9
    assert score_message("hello", False, 1) == 1
    assert score_message("hello", False, 0) == 0


def test_known_sender_score_is_clamped_and_can_remain_positive():
    assert score_message("hello", True, 0) == 0
    assert score_message("free winner urgent", True, 0) == 3


def test_classification_and_inbox_summary():
    assert classify(1) == "clean"
    assert classify(4) == "suspicious"
    assert classify(8) == "spam"

    counts = filter_inbox([
        ("hello", False, 0),
        ("free winner", False, 0),
        ("free winner prize urgent", False, 0),
    ])
    assert counts == {"spam": 1, "suspicious": 1, "clean": 1}
    assert inbox_status(counts) == "noisy"
    assert inbox_status({"spam": 2, "suspicious": 0, "clean": 1}) == "flooded"
    assert inbox_status({"spam": 1, "suspicious": 0, "clean": 4}) == "healthy"
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"
