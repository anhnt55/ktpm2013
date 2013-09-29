__author__ = "The Anh"
__project__ = "Test Triangle"

import unittest
import triangle
import math

class MyTest(unittest.TestCase):
    def test_triangle1(self):
        self.assertEqual(triangle.checkTriangle(3,4,5),'Tam giac vuong')
    def test_triangle2(self):
        self.assertEqual(triangle.checkTriangle(1,1,2),'Khong phai tam giac')
    def test_triangle3(self):
        self.assertEqual(triangle.checkTriangle(1,1,1),'Tam giac deu')
    def test_triangle4(self):
        self.assertEqual(triangle.checkTriangle(0,1,1),'Vuot qua mien gia tri')
    def test_triangle5(self):
        self.assertEqual(triangle.checkTriangle(2,3,2),'Tam giac can')
    def test_triangle6(self):
        self.assertEqual(triangle.checkTriangle(4,2,3),'Tam giac thuong')
    def test_triangle7(self):
        self.assertEqual(triangle.checkTriangle(pow(2,32),1,1),'Vuot qua mien gia tri')
    def test_triangle8(self):
        self.assertEqual(triangle.checkTriangle(1,1,math.sqrt(2)),'Tam giac vuong can')
    def test_triangle9(self):
        self.assertEqual(triangle.checkTriangle(-5,1,8),'Vuot qua mien gia tri')
    def test_triangle10(self):
        self.assertEqual(triangle.checkTriangle(pow(2,32)-2,pow(2,32)-2,pow(2,32)-2),'Tam giac deu')
    def test_triangle11(self):
        self.assertEqual(triangle.checkTriangle(pow(2,32)-1,pow(2,32)-2,pow(2,32)-2),'Tam giac can')
    def test_triangle12(self):
        self.assertEqual(triangle.checkTriangle(9/2,3,2),'Tam giac thuong')
if __name__ == '__main__':
    unittest.main()
