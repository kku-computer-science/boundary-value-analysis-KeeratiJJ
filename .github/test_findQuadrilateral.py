import unittest
from findQuadrilateral import Quadrilateral

class TestQuadrilateral(unittest.TestCase):

    def test_top1(self):
        quad = Quadrilateral(1, 100, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_top2(self):
        quad = Quadrilateral(2, 100, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")
    
    def test_top100(self):
        quad = Quadrilateral(100, 100, 100, 100)
        self.assertEqual(quad.classify(), "Square")
    
    def test_top199(self):
        quad = Quadrilateral(199, 100, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_top200(self):
        quad = Quadrilateral(200, 100, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

#===============================================================================================================#

    def test_left1(self):
        quad = Quadrilateral(100, 1, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_left2(self):
        quad = Quadrilateral(100, 2, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    # def test_left100(self):
    #     quad = Quadrilateral(100, 100, 100, 100)
    #     self.assertEqual(quad.classify(), "Square")

    def test_left199(self):
        quad = Quadrilateral(100, 199, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_left200(self):
        quad = Quadrilateral(100, 200, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

#===============================================================================================================#

    def test_bottom1(self):
        quad = Quadrilateral(100, 100, 1, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_bottom2(self):
        quad = Quadrilateral(100, 100, 2, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    # def test_bottom100(self):
    #     quad = Quadrilateral(100, 100, 100, 100)
    #     self.assertEqual(quad.classify(), "Square")

    def test_bottom199(self):
        quad = Quadrilateral(100, 100, 199, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_bottom200(self):
        quad = Quadrilateral(100, 100, 200, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

#===============================================================================================================#

    def test_right1(self):
        quad = Quadrilateral(100, 100, 100, 1)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_right2(self):
        quad = Quadrilateral(100, 100, 100, 2)
        self.assertEqual(quad.classify(), "Trapezoid")

    # def test_right100(self):
    #     quad = Quadrilateral(100, 100, 100, 100)
    #     self.assertEqual(quad.classify(), "Square")

    def test_right199(self):
        quad = Quadrilateral(100, 100, 100, 199)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_right200(self):
        quad = Quadrilateral(100, 100, 100, 200)
        self.assertEqual(quad.classify(), "Trapezoid")

if __name__ == '__main__':
    unittest.main()