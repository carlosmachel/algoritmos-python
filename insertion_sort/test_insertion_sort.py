
import unittest
''' Test for insertion_sort
'''

from insertion_sort import insertion_sort


class InsertionSortTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEquals(insertion_sort([]), [])

    def test_unordered_list(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_ordered_list(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unordered_list(self):
        self.assertEqual(insertion_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
