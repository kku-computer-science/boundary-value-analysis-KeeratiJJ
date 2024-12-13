import unittest
from findQuadrilateral import Quadrilateral

class TestQuadrilateral(unittest.TestCase):

    def test_Robust_top0(self):
        quad = Quadrilateral(0, 100, 100, 100)
        self.assertEqual(quad.classify(), "Error")

    def test_Robust_top1(self):
        quad = Quadrilateral(1, 100, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_top2(self):
        quad = Quadrilateral(2, 100, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_top100(self):
        quad = Quadrilateral(100, 100, 100, 100)
        self.assertEqual(quad.classify(), "Square")

    def test_Robust_top199(self):
        quad = Quadrilateral(199, 100, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_top200(self):
        quad = Quadrilateral(200, 100, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_top201(self):
        quad = Quadrilateral(201, 100, 100, 100)
        self.assertEqual(quad.classify(), "Error")

#===============================================================================================================#

    def test_Robust_left0(self):
        quad = Quadrilateral(100, 0, 100, 100)
        self.assertEqual(quad.classify(), "Error")

    def test_Robust_left1(self):
        quad = Quadrilateral(100, 1, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_left2(self):
        quad = Quadrilateral(100, 2, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    # def test_Robust_left100(self):
    #     quad = Quadrilateral(100, 100, 100, 100)
    #     self.assertEqual(quad.classify(), "Square")

    def test_Robust_left199(self):
        quad = Quadrilateral(100, 199, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_left200(self):
        quad = Quadrilateral(100, 200, 100, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_left201(self):
        quad = Quadrilateral(100, 201, 100, 100)
        self.assertEqual(quad.classify(), "Error")

#===============================================================================================================#

    def test_Robust_bottom0(self):
        quad = Quadrilateral(100, 1000, 0, 100)
        self.assertEqual(quad.classify(), "Error")

    def test_Robust_bottom1(self):
        quad = Quadrilateral(100, 100, 1, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_bottom2(self):
        quad = Quadrilateral(100, 100, 2, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    # def test_Robust_bottomt100(self):
    #     quad = Quadrilateral(100, 100, 100, 100)
    #     self.assertEqual(quad.classify(), "Square")

    def test_Robust_bottom199(self):
        quad = Quadrilateral(100, 100, 199, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_bottom200(self):
        quad = Quadrilateral(100, 100, 200, 100)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_bottom201(self):
        quad = Quadrilateral(100, 100, 201, 100)
        self.assertEqual(quad.classify(), "Error")

#===============================================================================================================#

    def test_Robust_right0(self):
        quad = Quadrilateral(100, 1000, 100, 0)
        self.assertEqual(quad.classify(), "Error")

    def test_Robust_right1(self):
        quad = Quadrilateral(100, 100, 100, 1)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_right2(self):
        quad = Quadrilateral(100, 100, 100, 2)
        self.assertEqual(quad.classify(), "Trapezoid")

    # def test_Robust_rightt100(self):
    #     quad = Quadrilateral(100, 100, 100, 100)
    #     self.assertEqual(quad.classify(), "Square")

    def test_Robust_right199(self):
        quad = Quadrilateral(100, 100, 100, 199)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_right200(self):
        quad = Quadrilateral(100, 100, 100, 200)
        self.assertEqual(quad.classify(), "Trapezoid")

    def test_Robust_right201(self):
        quad = Quadrilateral(100, 100, 100, 201)
        self.assertEqual(quad.classify(), "Error")


if __name__ == '__main__':
    unittest.main()


