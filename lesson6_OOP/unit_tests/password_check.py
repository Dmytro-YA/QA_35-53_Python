import unittest


def check_password_length(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    return True
class TestPassword(unittest.TestCase):
    def test_short_password_raises_error(self):
        with self.assertRaises(ValueError):
            check_password_length("short")

    def test_valid_password_returns_true(self):
        self.assertTrue(check_password_length("validpassword"))
