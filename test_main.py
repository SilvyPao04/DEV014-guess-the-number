"""Main test for the 'Guess the Number' game."""

import unittest
from unittest.mock import patch

from main import check_user_guess, computer_guess, random_generated_number, get_user_guess

class TestGame(unittest.TestCase):
    """Unit tests for the 'Guess the Number' game functions."""


    def test_check_user_guess(self):
        """Test the check_user_guess function."""
        # Test when the guess is too low
        self.assertEqual(check_user_guess(50, 100), (False, "low"))
        # Test when the guess is too high
        self.assertEqual(check_user_guess(150, 100), (False, "high"))
        # Test when the guess is correct
        self.assertEqual(check_user_guess(100, 100), (True, "correct"))

    def test_computer_guess(self):
        """Test the computer_guess function."""
        # Test if the guess is within the range
        min_val, max_val = 1, 100
        guess = computer_guess(min_val, max_val)
        self.assertTrue(min_val <= guess <= max_val)

    @patch('main.input', return_value='50')
    def test_get_user_guess(self, _mock_input):
        """Test the get_user_guess function."""
        # Test if the user's guess is correctly converted to an integer
        self.assertEqual(get_user_guess(), 50)

    @patch('main.random.randint', return_value=42)
    def test_random_generated_number(self, _mock_randint):
        """Test the random_generated_number function."""
        # Test if the random number generated is as expected
        self.assertEqual(random_generated_number(), 42)

if __name__ == "__main__":
    unittest.main()
