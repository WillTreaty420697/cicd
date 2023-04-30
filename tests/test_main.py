"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from main import is_odd, is_odd_str, is_square


class Test(TestCase):
    def test_is_odd(self):
        assert not is_odd(0)
        assert is_odd(1)
        assert not is_odd(2)

    def test_is_square(self):
        assert is_square(16)
        assert is_square(9)
        assert not is_square(-16) # Negatives of otherwise squares
        assert not is_square(-9)
        assert is_square(123456789**2) # Big numbers

    def test_is_odd_str(self):
        assert is_odd_str("0") == '0 is even and is a square.'
        assert is_odd_str("1") == '1 is odd and is a square.'
        assert is_odd_str("2") == '2 is even and is not a square.'
        assert is_odd_str("-1") == 'Please enter a number.'
        assert is_odd_str("A") == "Please enter a number."
        assert is_odd_str("") == "Please enter a number."