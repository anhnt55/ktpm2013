__author__ = "Nguyen The Anh"
__project__ = "Test Triangle"
__ID__ ="10020010"

import unittest
import triangle
import math

class MyTest(unittest.TestCase):
 
    #Kiem tra tam giac can
    def test1(self):
        self.assertEqual(triangle.detect_triangle(2,3,2),'Tam giac can')
    def test2(self):
        self.assertEqual(triangle.detect_triangle(pow(2,31)-1,pow(2,31)-2,pow(2,31)-2),'Tam giac can')
    def test3(self):
        self.assertEqual(triangle.detect_triangle(pow(2,26), pow(2,26), pow(1,-10)),'Tam giac can')
    def test4(self):
        self.assertEqual(triangle.detect_triangle(pow(2,31)-1, pow(2,31)-1, 1),'Tam giac can')
    #Kiem tra tam giac deu
    def test5(self):
        self.assertEqual(triangle.detect_triangle(1,1,1),'Tam giac deu')
    def test6(self):
        self.assertEqual(triangle.detect_triangle(pow(2,31)-1,pow(2,31)-1,pow(2,31)-1),'Tam giac deu')
    def test7(self):
        self.assertEqual(triangle.detect_triangle(pow(1,-40),pow(1,-40),pow(1,-40)),'Tam giac deu')
    #Kiem tra tam giac vuong
    def test8(self):
        self.assertEqual(triangle.detect_triangle(3,4,5),'Tam giac vuong')
    def test9(self):
        self.assertEqual(triangle.detect_triangle(3*pow(2,25),4*pow(2,25),5*pow(2,25)),'Tam giac vuong')
    def test10(self):
        self.assertEqual(triangle.detect_triangle(3*pow(1,-10),4*pow(1,-10),5*pow(1,-10)),'Tam giac vuong')
    #Kiem tra tam giac vuong can
    def test11(self):
        self.assertEqual(triangle.detect_triangle(1,1,math.sqrt(2)),'Tam giac vuong can')
    def test12(self):
        self.assertEqual(triangle.detect_triangle(3*math.sqrt(2),3,3),'Tam giac vuong can')
    def test13(self):
        self.assertEqual(triangle.detect_triangle(5,5*math.sqrt(2),5),'Tam giac vuong can')
    #Kiem tra tam giac thuong
    def test14(self):
        self.assertEqual(triangle.detect_triangle(4,2,3),'Tam giac thuong')    
    def test15(self):
        self.assertEqual(triangle.detect_triangle(9/2,3,2),'Tam giac thuong')
    def test16(self):
        self.assertEqual(triangle.detect_triangle(12345678,12345677,12345679),'Tam giac thuong')
    def test17(self):
        self.assertEqual(triangle.detect_triangle(pow(2,31)-1,pow(2,31)-2,pow(2,31)-3),'Tam giac thuong')
    #Kiem tra khong phai la tam giac
    def test18(self):
        self.assertEqual(triangle.detect_triangle(1,1,2),'Khong phai tam giac')
    def test19(self):
        self.assertEqual(triangle.detect_triangle(0,1,4),'Khong phai tam giac')
    def test20(self):
        self.assertEqual(triangle.detect_triangle(4,0,8),'Khong phai tam giac')
    def test21(self):
        self.assertEqual(triangle.detect_triangle(9,1,0),'Khong phai tam giac')
    def test22(self):
        self.assertEqual(triangle.detect_triangle(0,0,0),'Khong phai tam giac')
    def test23(self):
        self.assertEqual(triangle.detect_triangle(0,0,4),'Khong phai tam giac')
    def test24(self):
        self.assertEqual(triangle.detect_triangle(0,1,0),'Khong phai tam giac')
    def test25(self):
        self.assertEqual(triangle.detect_triangle(9,0,0),'Khong phai tam giac')
    #Kiem tra dau vao vuot qua gia tri
    def test26(self):
        self.assertEqual(triangle.detect_triangle(pow(2,32),1,1),'Vuot qua mien gia tri')
    def test27(self):
        self.assertEqual(triangle.detect_triangle(1,pow(2,32),1),'Vuot qua mien gia tri')
    def test28(self):
        self.assertEqual(triangle.detect_triangle(1,1,pow(2,32)),'Vuot qua mien gia tri')
    def test29(self):
        self.assertEqual(triangle.detect_triangle(-1,4,5),'Vuot qua mien gia tri')
    def test30(self):
        self.assertEqual(triangle.detect_triangle(6,-4,5),'Vuot qua mien gia tri')
    def test31(self):
        self.assertEqual(triangle.detect_triangle(8,4,-5),'Vuot qua mien gia tri')
    def test32(self):
        self.assertEqual(triangle.detect_triangle(-1,-4,5),'Vuot qua mien gia tri')
    def test33(self):
        self.assertEqual(triangle.detect_triangle(-1,-4,-5),'Vuot qua mien gia tri')
    
if __name__ == '__main__':
    unittest.main()
