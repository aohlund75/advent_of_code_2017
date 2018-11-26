import unittest
from puzzle2_2 import product_of_dividers
from puzzle2_2 import read_file_as_int_matrix

class PuzzelTest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(4, product_of_dividers([5,9,2,8]))
    
    def test_case_2(self):
        self.assertEqual(3, product_of_dividers([9,4,7,3]))
    
    def test_case_3(self):
        self.assertEqual(2, product_of_dividers([3,8,6,5]))
    
    def test_read_file(self): 
        matrix = read_file_as_int_matrix('test_input.txt')
        self.assertEqual(3, len(matrix))
        self.assertEqual(3, len(matrix[0]))
        self.assertEqual(1, matrix[0][0])
        self.assertEqual(4, matrix[1][0])
    