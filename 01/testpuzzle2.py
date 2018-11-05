import unittest
from puzzle1_2 import calculate_sum


#The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits 
#1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
#1221 produces 0, because every comparison is between a 1 and a 2.
#123425 produces 4, because both 2s match each other, but no other digit has a match.
#123123 produces 12.
#12131415 produces 4.
class PuzzelTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(6, calculate_sum([1,2,1,2]))
    
    def test_case2(self):
        self.assertEqual(0, calculate_sum([1,2,2,1]))
    
    def test_case3(self):
        self.assertEqual(4, calculate_sum([1,2,3,4,2,5]))
    
    def test_case4(self):
        self.assertEqual(4, calculate_sum([1,2,1,3,1,4,1,5]))
        
        
