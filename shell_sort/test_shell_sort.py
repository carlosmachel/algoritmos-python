import unittest
''' Test for shell_sort
'''

from shell_sort import shell_sort


class ShellSortTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEquals(shell_sort([]), [])

    def test_unordered_list(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_ordered_list(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
