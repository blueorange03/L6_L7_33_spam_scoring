# L6_L7_33 — Spam Scoring Filter

Lab 6: Code and Branch Coverage

## About

A small Python module that scores messages for spam signals, classifies them and summarises the state of an inbox.

## Files

| File | Description |
|------|-------------|
| `spam_scoring.py` | The module under test |
| `CodeCoverageTest_33_application.py` | Line coverage cases |
| `BranchCoverageTest_33_application.py` | Branch coverage cases |

Refer to the lab handout for instructions.

## Run the coverage suites

Create and activate a local environment, then install the tools:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest coverage
```

Line coverage:

```sh
coverage run -m pytest CodeCoverageTest_33_application.py
coverage report -m --include=spam_scoring.py
```

Branch coverage:

```sh
coverage erase
coverage run --branch -m pytest BranchCoverageTest_33_application.py
coverage report -m --include=spam_scoring.py
```

The handout requires a terminal screenshot of each final report. Capture the
line report after the first pair of commands and the branch report after the
second pair.
