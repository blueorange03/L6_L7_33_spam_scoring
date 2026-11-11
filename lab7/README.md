# L6_L7_33 — Spam Scoring Filter

Lab 7: Fuzz Testing with Hypothesis

## About

A small Python module that parses sender addresses, finds the first HTTP(S) link in a message, and measures the uppercase share of its letters. The helpers are hardened against malformed values and non-string input.

## Files

| File | Description |
|------|-------------|
| `spam_scoring.py` | Defensive application code under test |
| `test_spam_scoring.py` | Hypothesis no-crash fuzz tests for all three helpers |
