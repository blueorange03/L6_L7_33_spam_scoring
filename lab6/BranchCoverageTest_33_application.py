"""Branch-coverage suite for every decision in the spam scoring application."""

import pytest

from spam_scoring import classify, filter_inbox, inbox_status, score_message


@pytest.mark.parametrize(
    ("text", "known", "links", "expected"),
    [
        ("free", False, 0, 2),                 # spam word, no uppercase fallback
        ("LOUD", False, 0, 1),                  # uppercase fallback is true
        ("hello", False, 0, 0),                 # ordinary word fallback is false
        ("WOW", False, 0, 0),                   # uppercase but too short
        ("hello", False, 4, 4),                 # link_count > 3
        ("hello", False, 1, 1),                 # 0 < link_count <= 3
        ("hello", False, 0, 0),                 # link_count == 0
        ("hello", True, 0, 0),                  # known sender, negative score clamped
        ("free winner urgent", True, 0, 3),     # known sender, score stays positive
        ("hello", False, 0, 0),                 # unknown sender
    ],
)
def test_score_message_decision_outcomes(text, known, links, expected):
    assert score_message(text, known, links) == expected


@pytest.mark.parametrize(
    ("score", "expected"),
    [(8, "spam"), (4, "suspicious"), (3, "clean")],
)
def test_classify_decision_outcomes(score, expected):
    assert classify(score) == expected


def test_filter_inbox_with_and_without_messages():
    assert filter_inbox([]) == {"spam": 0, "suspicious": 0, "clean": 0}
    assert filter_inbox([("free winner urgent", False, 4)]) == {
        "spam": 1,
        "suspicious": 0,
        "clean": 0,
    }


@pytest.mark.parametrize(
    ("counts", "expected"),
    [
        ({"spam": 0, "suspicious": 0, "clean": 0}, "empty"),
        ({"spam": 2, "suspicious": 0, "clean": 1}, "flooded"),
        ({"spam": 1, "suspicious": 0, "clean": 2}, "noisy"),
        ({"spam": 1, "suspicious": 0, "clean": 4}, "healthy"),
    ],
)
def test_inbox_status_decision_outcomes(counts, expected):
    assert inbox_status(counts) == expected
