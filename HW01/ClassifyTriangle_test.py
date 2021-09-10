"""
Tyler Marchiano
SSW 567
HW01: Testing Triangle Classification
09.10.2021
"""

import sys
import unittest 
from ClassifyTriangle import classify_triangle

class TriangleTest(unittest.TestCase):
    '''
    This is a test class to test the features of the Triangle program
    '''
    
    
    def test_classify_triangle(self) -> None:
        '''testing classify_triangle'''
        #Testing Good Values
        self.assertEqual(classify_triangle(3,4,5), "Right Scalene Triangle")
        self.assertEqual(classify_triangle(3.6,3.6,3.6), "Equilateral Triangle")
        self.assertEqual(classify_triangle(7.1,4.3,5), "Scalene Triangle")
        self.assertEqual(classify_triangle(1,1,5), "Isosceles Triangle")
        
        #Testing Bad Values
        self.assertNotEqual(classify_triangle(-1,1,5), "Scalene")   #This throws an error since negative input
        #self.assertNotEqual(classify_triangle('hi',1,5), "Scalene") #This throws an error since input is not a number
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)