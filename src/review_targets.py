"""
INTENTIONAL BUG FIXTURES — AI Code Review E2E TEST.

This module contains deliberate defects for testing automated code review.
Do not use these functions in production.
"""

import json


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    # INTENTIONAL BUG: empty input causes ZeroDivisionError.
    return sum(numbers) / len(numbers)


def validate_age(age):
    """Validate an age supplied by an external caller."""
    # INTENTIONAL BUG: bool is a subclass of int in Python.
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    return age >= 18


def load_user_profile(file_path):
    """Load a user profile from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        # INTENTIONAL BUG: hides permission, parsing, and other errors.
        return None


def safe_divide(numerator, denominator):
    """Control function: safely divide two numbers."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")

    return numerator / denominator
