# shell_sort/test_shell_sort.py

import unittest
from shell_sort.shell_sort import shell_sort

class TestShellSort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_already_sorted_array(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(shell_sort([5, 2, 8, 3, 1]), [1, 2, 3, 5, 8])

if __name__ == '__main__':
    unittest.main()