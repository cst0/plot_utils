#!/usr/bin/env python3

import unittest
import sys
sys.path.append('..')
from utils.convert import numparse


class NumparseTestCase(unittest.TestCase):
    def test_simple_addition(self):
        # simplest case first
        result = numparse("10+5")
        self.assertEqual(result, (10 + 5))

        # checking 0's
        result = numparse("0+80")
        self.assertEqual(result, (0 + 80))

        result = numparse("80+0")
        self.assertEqual(result, (80 + 0))

        # different combinations of floats
        result = numparse("10.5+5.3")
        self.assertEqual(result, (10.5 + 5.3))

        result = numparse("10.5+5")
        self.assertEqual(result, (10.5 + 5))

        result = numparse("10+5.3")
        self.assertEqual(result, (10 + 5.3))

    def test_simple_subtraction(self):
        # simplest case first
        result = numparse("10-5")
        self.assertEqual(result, (10 - 5))

        # checking 0's
        result = numparse("0-80")
        self.assertEqual(result, (0 - 80))

        result = numparse("80-0")
        self.assertEqual(result, (80 - 0))

        # different combinations of floats
        result = numparse("10.5-5.3")
        self.assertEqual(result, (10.5 - 5.3))

        result = numparse("10.5-5")
        self.assertEqual(result, (10.5 - 5))

        result = numparse("10-5.3")
        self.assertEqual(result, (10 - 5.3))

    def test_simple_division(self):
        # simplest case first
        result = numparse("10/5")
        self.assertEqual(result, (10 / 5))

        # checking 0's
        result = numparse("0/80")
        self.assertEqual(result, (0 / 80))

        # different combinations of floats
        result = numparse("10.5/5.3")
        self.assertEqual(result, (10.5 / 5.3))

        result = numparse("10.5/5")
        self.assertEqual(result, (10.5 / 5))

        result = numparse("10/5.3")
        self.assertEqual(result, (10 / 5.3))

    def test_simple_multiplication(self):
        # simplest case first
        result = numparse("10*5")
        self.assertEqual(result, (10 * 5))

        # checking 0's
        result = numparse("0*80")
        self.assertEqual(result, (0 * 80))

        result = numparse("80*0")
        self.assertEqual(result, (80 * 0))

        # different combinations of floats
        result = numparse("10.5*5.3")
        self.assertEqual(result, (10.5 * 5.3))

        result = numparse("10.5*5")
        self.assertEqual(result, (10.5 * 5))

        result = numparse("10*5.3")
        self.assertEqual(result, (10 * 5.3))

if __name__ == '__main__':
    unittest.main()
