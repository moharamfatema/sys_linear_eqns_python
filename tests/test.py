import unittest
import numpy

from src import methods

class TestMethods(unittest.TestCase):
    
    def testGaussElimination(self):
        a = numpy.array([[2, 1, 4, 1], [1, 2, 3, 1.5], [4, -1 ,2, 2]])
        correct = numpy.matrix("-1;1;-0.5")
        x = methods.gauss_elimination(number_of_equations=3,input_equations=a)
        self.assertEqual(x.all(),correct.all())
        
        a = numpy.array([[4,6,2,-2,8],[2,0,5,-3,4],[-4,-3,-5,4,1],[8,18,-2,3,40]])
        correct = numpy.array([9,-6,3,2])
        x = methods.gauss_elimination(number_of_equations=4,input_equations=a)
        self.assertEqual(x.all(),correct.all())

        a[0][0] = 0
        with self.assertRaises(ZeroDivisionError):
            methods.gauss_elimination(number_of_equations=4,input_equations=a)




    