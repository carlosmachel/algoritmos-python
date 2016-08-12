import unittest
''' Test for bubble_sort
'''

from bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEquals(bubble_sort(''), '')

    def test_unordered_list(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
