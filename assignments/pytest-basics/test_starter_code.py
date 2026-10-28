import pytest


def is_even(number):
    return number % 2 == 0


def calculate_average(numbers):
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")
    return sum(numbers) / len(numbers)


def test_is_even_returns_true_for_even_number():
    assert is_even(4) is True