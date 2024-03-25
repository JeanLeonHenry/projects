import unittest

from chap1ex5 import one_away


class TestOneAway(unittest.TestCase):
    def test(self):
        fixture = [
            ("pale", "ple", True),
            ("pale", "pte", False),
            ("pales", "pale", True),
            ("pale", "bale", True),
            ("pale", "bake", False),
            ("", "a", True),
            ("gfvyujezaovifej", "ofefief", False),
        ]
        for *input, result in fixture:
            with self.subTest(input=input):
                try:
                    self.assertEqual(one_away(*input), result)
                except AssertionError:
                    raise AssertionError("/".join(input))
