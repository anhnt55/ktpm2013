__author__ = "Nguyen The Anh"
__project__ = "Test Triangle"

import unittest
import triangle
import math

class MyTest(unittest.TestCase):
    def test_triangle1(self):
        self.assertEqual(triangle.detect_triangle(3,4,5),'Tam giac vuong')
    def test_triangle2(self):
        self.assertEqual(triangle.detect_triangle(1,1,2),'Khong phai tam giac')
    def test_triangle3(self):
        self.assertEqual(triangle.detect_triangle(1,1,1),'Tam giac deu')
    def test_triangle4(self):
        self.assertEqual(triangle.detect_triangle(0,1,1),'Vuot qua mien gia tri')
    def test_triangle5(self):
        self.assertEqual(triangle.detect_triangle(2,3,2),'Tam giac can')
    def test_triangle6(self):
        self.assertEqual(triangle.detect_triangle(4,2,3),'Tam giac thuong')
    def test_triangle7(self):
        self.assertEqual(triangle.detect_triangle(pow(2,32),1,1),'Vuot qua mien gia tri')
    def test_triangle8(self):
        self.assertEqual(triangle.detect_triangle(1,1,math.sqrt(2)),'Tam giac vuong can')
    def test_triangle9(self):
        self.assertEqual(triangle.detect_triangle(-5,1,8),'Vuot qua mien gia tri')
    def test_triangle10(self):
        self.assertEqual(triangle.detect_triangle(pow(2,32)-2,pow(2,32)-2,pow(2,32)-2),'Tam giac deu')
    def test_triangle11(self):
        self.assertEqual(triangle.detect_triangle(pow(2,32)-1,pow(2,32)-2,pow(2,32)-2),'Tam giac can')
    def test_triangle12(self):
        self.assertEqual(triangle.detect_triangle(9/2,3,2),'Tam giac thuong')
    def test_triangle13(self):
        self.assertEqual(triangle.detect_triangle(pow(10,-10),pow(10,-10),pow(10,-10)),'Tam giac deu')
    def test_triangle14(self):
        self.assertEqual(triangle.detect_triangle(12345678,12345677,12345679),'Tam giac thuong')
    def test_triangle15(self):
        self.assertEqual(triangle.detect_triangle(5,0,7),'Vuot qua mien gia tri')
    def test_triangle16(self):
        self.assertEqual(triangle.detect_triangle(8,5,0),'Vuot qua mien gia tri')
    def test_triangle17(self):
        self.assertEqual(triangle.detect_triangle(8,-1,8),'Vuot qua mien gia tri')
    def test_triangle18(self):
        self.assertEqual(triangle.detect_triangle(200,1,-8),'Vuot qua mien gia tri')
    def test_triangle19(self):
        self.assertEqual(triangle.detect_triangle(7,pow(2,33),8),'Vuot qua mien gia tri')
    def test_triangle20(self):
        self.assertEqual(triangle.detect_triangle(6,100,pow(2,35)),'Vuot qua mien gia tri')
    def test_triangle21(self):
        self.assertEqual(triangle.detect_triangle(3*math.sqrt(2),3,3),'Tam giac vuong can')
    def test_triangle22(self):
        self.assertEqual(triangle.detect_triangle(5,5,5*math.sqrt(2)),'Tam giac vuong can')
    def test_triangle23(self):
        self.assertEqual(triangle.detect_triangle(math.sqrt(2),math.sqrt(2),math.sqrt(2)),'Tam giac deu')
    def test_triangle24(self):
        self.assertEqual(triangle.detect_triangle(-5,1,8),'Vuot qua mien gia tri')
if __name__ == '__main__':
    unittest.main()
