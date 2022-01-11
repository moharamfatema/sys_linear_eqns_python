import unittest
import numpy
import numpy.testing as npt
import os
from src import methods, parse

class TestMethods(unittest.TestCase):
        
    def testGaussElimination(self):
        a = numpy.array([[2, 1, 4, 1], [1, 2, 3, 1.5], [4, -1 ,2, 2]])
        correct = numpy.array([1,1,-0.5])
        x = methods.gauss_elimination(number_of_equations=3,input_equations=a).get('solution')
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_equal(x ,correct )

        a = numpy.array([
            [4,6,2,-2,8],
            [2,0,5,-2,4],
            [-4,-3,-5,4,1],
            [8,18,-2,3,40]
            ])
        correct = numpy.array([-13.5,8+2/3,7,2])
        x = methods.gauss_elimination(number_of_equations=4,input_equations=a).get('solution')
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_equal(x ,correct )

        a[0][0] = 0
        with self.assertRaises(ZeroDivisionError):
            methods.gauss_elimination(number_of_equations=4,input_equations=a)

        a = numpy.array([[1,2,5,-1,7,1],[0,-8,5,0,10,5],[0,-4,5,6,1,3],[0,6,25,99,2,4],[0,0,33,2,15,2]])
        correct = numpy.array([1.939052136,-0.5869276124,1737/31207.0,3863/62414.0,82/31207.0])
        x = methods.gauss_elimination(number_of_equations=5,input_equations=a).get('solution')
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x ,correct ,5)


    def testLU(self):
        a = numpy.array([[2, 1, 4, 1], [1, 2, 3, 1.5], [4, -1 ,2, 2]])
        correct = numpy.array([1,1,-0.5])
        x = methods.LU(number_of_equations=3,input_equations=a).get('solution')
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x ,correct ,5)

        a = numpy.array([[4,6,2,-2,8],[2,0,5,-2,4],[-4,-3,-5,4,1],[8,18,-2,3,40]])
        correct = numpy.array([-13.5,8+2/3,7,2])
        x = methods.LU(number_of_equations=4,input_equations=a).get('solution')
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x ,correct ,5)

        a = numpy.array([[1,2,5,-1,7,1],[0,-8,5,0,10,5],[0,-4,5,6,1,3],[0,6,25,99,2,4],[0,0,33,2,15,2]])
        correct = numpy.array([1.939052136,-0.5869276124,1737/31207.0,3863/62414.0,82/31207.0])
        x = methods.LU(number_of_equations=5,input_equations=a).get('solution')
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x ,correct ,5)

        temp = a[0]
        a[0] = a[4]
        a[4] = temp

        temp = correct[0]
        correct[0] = correct[4]
        correct[4] = temp
        x = methods.LU(number_of_equations=5,input_equations=a).get('solution')
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x ,correct ,5)

    def testGaussJordan(self):
        a = numpy.array([[2, 1, 4, 1], [1, 2, 3, 1.5], [4, -1 ,2, 2]])
        correct = numpy.array([1,1,-0.5])
        x = methods.gauss_jordan(number_of_equations=3,input_equations=a)
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x ,correct ,5)

        a = numpy.array([[4,6,2,-2,8],[2,0,5,-2,4],[-4,-3,-5,4,1],[8,18,-2,3,40]])
        correct = numpy.array([-13.5,8+2/3,7,2])
        x = methods.gauss_elimination(number_of_equations=4,input_equations=a)
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x,correct ,5)

        a[0][0] = 0
        with self.assertRaises(ZeroDivisionError):
            methods.gauss_jordan(number_of_equations=4,input_equations=a)

        a = numpy.array([[1,2,5,-1,7,1],[0,-8,5,0,10,5],[0,-4,5,6,1,3],[0,6,25,99,2,4],[0,0,33,2,15,2]])
        correct = numpy.array([1.939052136,-0.5869276124,1737/31207.0,3863/62414.0,82/31207.0])
        x = methods.gauss_elimination(number_of_equations=5,input_equations=a)
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x ,correct ,5)

    def testGaussSiedel(self):
        a = numpy.array([[2, 1, 4], [1, 2, 3], [4, -1 ,2]])
        b = numpy.array([1,1.5,2])
        correct = numpy.array([1,1,-0.5])
        x = methods.gauss_seidel(a,b)
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x,correct,5)

        a = numpy.array([[4,6,2,-2],[2,0,5,-2],[-4,-3,-5,4],[8,18,-2,3]])
        b = numpy.array([8,4,1,40])
        correct = numpy.array([-13.5,8+2/3,7,2])
        x = methods.gauss_seidel(a,b)
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x,correct,5)

        a = numpy.array([[1,2,5,-1,7],[0,-8,5,0,10],[0,-4,5,6,1],[0,6,25,99,2],[0,0,33,2,15]])
        b = numpy.array([1,5,3,4,2])
        correct = numpy.array([1.939052136,-0.5869276124,1737/31207.0,3863/62414.0,82/31207.0])
        x = methods.gauss_seidel(a,b)
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x,correct,5)

        temp = a[0]
        a[0] = a[4]
        a[4] = temp

        temp = correct[0]
        correct[0] = correct[4]
        correct[4] = temp

        temp = b[0]
        b[0] = b[4]
        b[4] = temp

        x = methods.gauss_seidel(a,b)
        self.assertEqual(x.shape,correct.shape)
        npt.assert_array_almost_equal(x,correct,5)

class TestParse(unittest.TestCase):
    
    def testFromFile(self):
        info = {
            'no of Equations':3,
            'method':"Gaussian-siedel",
            'equations':['3*a + 2*b + c - 6','2*a + 3*b - 7','2*c - 4'],
            'initial values':[1,1.1,2],
            'max iterations':50,
            'epsilon':1e-5
        }
        x = parse.fromFile("tests\\in\\gaussSiedelSample.txt")
        self.assertDictEqual(x,info)
    
    def testGetCoeff(self):
        info = {
            'no of Equations':3,
            'method':"Gaussian-siedel",
            'equations':['3*a + 2*b + c - 6','2*a + 3*b - 7','2*c - 4'],
            'initial values':[1,1.1,2]
        }
        a,b,aug = parse.getCoeff(info)
        npt.assert_array_equal(a,[[3,2,1],[2,3,0],[0,0,2]])
        npt.assert_array_equal(b,[6,7,4])
        npt.assert_array_equal(aug,[[3,2,1,6],[2,3,0,7],[0,0,2,4]])
        
    