"""Hypothesis tests for the three public spam scoring helpers."""

from hypothesis import given, strategies as st

from spam_scoring import first_link, sender_domain, shout_ratio


@given(st.text() | st.none())
def test_sender_domain_no_crash(value):
    try:
        sender_domain(value)
    except Exception as exc:
        assert False, f"sender_domain crashed with: {exc}"


@given(st.text() | st.none())
def test_first_link_no_crash(value):
    try:
        first_link(value)
    except Exception as exc:
        assert False, f"first_link crashed with: {exc}"


@given(st.text() | st.none())
def test_shout_ratio_no_crash(value):
    try:
        shout_ratio(value)
    except Exception as exc:
        assert False, f"shout_ratio crashed with: {exc}"
