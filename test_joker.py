#!/usr/bin/env python
"""Test our jokes."""

import unittest
import joker


class TestUtils(unittest.TestCase):
    """Our tests."""

    def test_has_enough_jokes(self):
        """We need at least 400 jokes"""
        self.assertGreaterEqual(len(joker.get_jokes()), 400)


if __name__ == "__main__":
    unittest.main()
