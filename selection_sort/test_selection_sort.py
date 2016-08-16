import unittest
''' Test for selection_sort
'''

from selection_sort import selection_sort


class SelectionSortTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEquals(selection_sort([]), [])

    def test_unordered_list(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_ordered_list(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
