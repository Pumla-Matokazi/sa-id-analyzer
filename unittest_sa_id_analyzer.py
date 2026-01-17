import unittest
from sa_id_analyzer import (
    validate_birthdate,
    extract_gender,
    extract_citizenship
)


class TestSAIDAnalyzer(unittest.TestCase):

    def test_valid_birthdate(self):
        self.assertTrue(validate_birthdate("9902154800081"))

    def test_invalid_birthdate(self):
        self.assertFalse(validate_birthdate("9913324800081"))

    def test_gender_female(self):
        self.assertEqual(extract_gender("9902154800081"), "Female")

    def test_gender_male(self):
        self.assertEqual(extract_gender("9902155800081"), "Male")

    def test_citizenship_sa(self):
        self.assertEqual(extract_citizenship("9902154800081"), "South African")

    def test_citizenship_resident(self):
        self.assertEqual(extract_citizenship("9902154800181"), "Non-South African")


if __name__ == "__main__":
    unittest.main()
