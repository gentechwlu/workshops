"""
Author: Yoseph Tamene
Workshop Head - GenTech
WLU '22
"""

import unittest
from Questions import (longest_sequence, product_list)

class TestProductList(unittest.TestCase):

    def test_product_list(self):
        self.assertEqual(product_list.getProductList([1,2,3,4]), [24,12,8,6])
        self.assertEqual(product_list.getProductList([2,2,2,2,2]), [16,16,16,16,16])
        self.assertEqual(product_list.getProductList([2]), [1])

    def test_product_list_division(self):
        self.assertEqual(product_list.getProductListDivision([1,2,3,4]), [24,12,8,6])
        self.assertEqual(product_list.getProductListDivision([2,2,2,2,2]), [16,16,16,16,16])
        self.assertEqual(product_list.getProductListDivision([2]), [1])

    def test_product_list_fast(self):
        self.assertEqual(product_list.getProductList_fast([1,2,3,4]), [24,12,8,6])
        self.assertEqual(product_list.getProductList_fast([2,2,2,2,2]), [16,16,16,16,16])
        self.assertEqual(product_list.getProductList_fast([2]), [1])

class TestLongestSequence(unittest.TestCase):

    def test_longest_sequence(self):
        self.assertEqual(longest_sequence.longestSequence([3,5,6,2,3,4,5]), 5)
        self.assertEqual(longest_sequence.longestSequence([2,1,4,5]), 2)
        self.assertEqual(longest_sequence.longestSequence([5]), 1)

    def test_longest_sequence_fast(self):
        self.assertEqual(longest_sequence.longestSequence_fast([3,5,6,2,3,4,5]), 5)
        self.assertEqual(longest_sequence.longestSequence_fast([2,1,4,5]), 2)
        self.assertEqual(longest_sequence.longestSequence_fast([5]), 1)
        
    


if __name__ == "__main__":
    unittest.main()