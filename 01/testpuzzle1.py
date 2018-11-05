import unittest
from puzzle1_1 import calculate_sum


#The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits 
# that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.
#
#For example:
#
#1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
#1111 produces 4 because each digit (all 1) matches the next.
#1234 produces 0 because no digit matches the next.
#91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
class PuzzelTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(3, calculate_sum([1,1,2,2]))
    
    def test_case2(self):
        self.assertEqual(4, calculate_sum([1,1,1,1]))
    
    def test_case3(self):
        self.assertEqual(0, calculate_sum([1,2,3,4]))
    
    def test_case4(self):
        self.assertEqual(9, calculate_sum([9,1,2,1,2,1,2,9]))
        
        
