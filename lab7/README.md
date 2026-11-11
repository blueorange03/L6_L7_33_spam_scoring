# L6_L7_33 — Spam Scoring Filter

Lab 7: Fuzz Testing with Hypothesis

## About

A small Python module that parses sender addresses, finds the first HTTP(S) link in a message, and measures the uppercase share of its letters. The helpers are hardened against malformed values and non-string input.

## Files

| File | Description |
|------|-------------|
| `spam_scoring.py` | Defensive application code under test |
| `test_spam_scoring.py` | Hypothesis no-crash fuzz tests for all three helpers |

## Install and run

From this directory, create an environment and install the two handout dependencies:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install hypothesis pytest
```

Run the interactive application:

```sh
python spam_scoring.py
```

Run the fuzz tests:

```sh
python -m pytest -q test_spam_scoring.py
```

## Lab 7 screenshots and submission

The handout asks for a PDF containing these four terminal screenshots, captured in order:

1. **Before fix — application:** run `python spam_scoring.py`, enter `offers@Deals.com`, `Visit https://example.com now`, and `FREE prize NOW`; capture the complete output.
2. **Before fix — failing fuzz tests:** use the original buggy `spam_scoring.py` with the completed tests, run `python -m pytest -q test_spam_scoring.py`, and capture the failure summary and Hypothesis examples. The original `first_link` and `shout_ratio` crash on strings without an HTTP link and strings with no letters. The starter `sender_domain` also crashes for `None` or an address without `@`.
3. **After fix — application:** run the same three application inputs against the fixed script and capture the complete output.
4. **After fix — passing fuzz tests:** run `python -m pytest -q test_spam_scoring.py` against the fixed script and capture the passing summary.

The submission consists of the PDF with all four screenshots, `spam_scoring.py`, and `test_spam_scoring.py`. Keep screenshots legible and show the command and its result in each terminal capture. Preserve the pre-fix failing run before replacing the starter script; it cannot be reproduced from the final fixed files alone.
