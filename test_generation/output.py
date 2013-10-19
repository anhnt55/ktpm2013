__author__ = 'theanh'
#mssv :10020010
#file "output.py"

import input
import unittest
import inspect
import itertools
import random

array = []     #mang chua cac dieu kien dau vao
arrayTest = [] #mang chua cac test case

doc = input.main.__doc__

i = 0;
j = -1;
#Doc cac chuoi tu file input vao va dua cac gia tri vao mang array va arrayTest
while( i < len( doc ) ):
    val_1 = ''
    val_2 = ''
    if(doc[i]=='['):#khi gap dau mo ngoac [
        n = i + 1
        while( doc[n] != ';' ): #khi gap dua ; ngan giua 2 gia tri dau mut cua doan
            val_1 += doc[n]
            n = n + 1
        a = int( val_1 )
        val_1 = ''
        n = n + 1

        while( doc[n] != ']' ):#khi gap dau dong ngoac ]
            val_2 += doc[n]
            n = n + 1
        b = int( val_2 )
        val_2 = ''
        array[j].append(a); #them phan tu a vao cuoi mang
        array[j].append(b); #them phan tu b vao cuoi mang
        arrayTest[j].append(random.randint(a,b)) #them phan tu duoc lay random tu [a,b] va them vao mang arrayTest
    if(( i + 1 ) < len( doc ) and doc[i + 1]==':'):#neu gap bien tiep theo
        j = j + 1
        array.append([])
        arrayTest.append([])
    i = i + 1

#sap xep tang dan dau mut cua cac doan
for sub_array in array: #lay ra cac mang nho (tuong ung voi cac bien dau vao a,b,c)
    for i in range(0, len(sub_array)):
        for j in range(i + 2, len(sub_array)):
            if(sub_array[i] > sub_array[j]):
                #------ sap xep dau mut a -------
                a = array[i]
                array[i] = array[j]
                array[j] = a
                #------ sap xep dau mut b -------
                b = array[i + 1]
                array[i + 1] = array[j + 1]
                array[j + 1] = b

#bien de kiem tra xem co dung dieu kien là lop tuong duong hay khong
checkCondition = True
#kiem tra dieu kien tuong duong
for sub_array in array:
    for i in range(0, len(sub_array) - 1):
        if ( sub_array[i] >= sub_array[i + 1] ):
            checkCondition = False
            break
#tong so testcase
numberOfTestCase = 1
for sub_array in arrayTest:
    numberOfTestCase = numberOfTestCase*len(sub_array)

#sinh testcase tu dong
class TestSequense(unittest.TestCase):
    pass

def test_generator(*args):
    def test(self):
        self.assertEqual(input.main(*args),"Hello world!")
    return test

if __name__ == '__main__':
    #in ra mang chua cac dieu kien ban dau
    print "\nArray is : "
    print array
    #in ra mang chua cac test case
    print "\nArrayTest is : "
    print arrayTest
    #in ra tong so test case
    print "\nTotal Test Case: "
    print numberOfTestCase

    if( checkCondition == True):
        print "Test case :\n"
        for element in itertools.product(*arrayTest):
            print element  #in ra cac test case
            test_name = 'test_%s' %str(element)
            test = test_generator(*element)
            setattr(TestSequense, test_name, test)
        unittest.main()
    else:
        raise Exception("Khong phai tuong duong")
