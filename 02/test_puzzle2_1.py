import unittest
from puzzle2_1 import dif_max_min
from puzzle2_1 import read_file_as_int_matrix

class PuzzelTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(8, dif_max_min([5,1,9,5]))
    
    def test_case2(self):
        self.assertEqual(4, dif_max_min([7,5,3]))

    def test_case3(self):
        self.assertEqual(6, dif_max_min([2,4,6,8]))

    def test_read_file(self): 
        matrix = read_file_as_int_matrix('test_input.txt')
        self.assertEqual(3, len(matrix))
        self.assertEqual(3, len(matrix[0]))
        self.assertEqual(1, matrix[0][0])
        self.assertEqual(4, matrix[1][0])
    