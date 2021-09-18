# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    #Test ID 1
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    #Test ID 2
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    #Test ID 3
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
    
    #Test ID 4 
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    #Test ID 5
    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(4,2,3),'Scalene','4,2,3 should be scalene')
    
    #Test ID 6
    def testIsocelesTriangle1(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be isoceles')
    
    #Test ID 7
    def testIsocelesTriangle2(self): 
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 should be isoceles')
    
    #Test ID 8
    def testIsocelesTriangle3(self): 
        self.assertEqual(classifyTriangle(3,2,2),'Isoceles','3,2,2 should be isoceles')
    
    #Test ID 9
    def testIsocelesTriangle4(self): 
        self.assertEqual(classifyTriangle(200,199,200),'Isoceles','200,199,200 should be isoceles')
    
    #Test ID 10
    def testFailure1(self): 
        self.assertEqual(classifyTriangle(201,1,1),'InvalidInput','201,1,1 should be InvalidInput')
    
    #Test ID 11
    def testFailure2(self): 
        self.assertEqual(classifyTriangle(150,1,1),'NotATriangle','150,1,1 should be NotATriangle')
    
    #Test ID 12
    def testFailure3(self): 
        self.assertEqual(classifyTriangle(0,3,4),'InvalidInput','0,3,4 should be InvalidInput')
    
    #Test ID 13
    def testFailure4(self): 
        self.assertEqual(classifyTriangle(3,0,4),'InvalidInput','3,0,4 should be InvalidInput')
    
    #Test ID 14
    def testFailure5(self): 
        self.assertEqual(classifyTriangle(4,3,0),'InvalidInput','4,3,0 should be InvalidInput')
    
    #Test ID 15
    def testFailure6(self): 
        self.assertEqual(classifyTriangle(0,5.5,4),'InvalidInput','0,5.5,4 should be InvalidInput')
    
    #Test ID 16
    def testFailure7(self): 
        self.assertEqual(classifyTriangle(0,5.5,3.1),'InvalidInput','0,5.5,3.1 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

