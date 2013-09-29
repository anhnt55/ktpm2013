import math

def checkTriangle(a, b, c):
    ep = pow(10,-9)
    if((a <= 0)|(b <= 0)|(c <= 0)|(a > pow(2,32)-1)|(c > pow(2,32)-1)|(c > pow(2,32)-1)):
        return "Vuot qua mien gia tri"
    else:
        if((a+b>c)&(b+c>a)&(a+c>b)):
            if((a == b)&(b == c)):
                return "Tam giac deu"
            else:
                if((a == b)|(b == c)|(a == c)):
                    if((math.fabs(a*a+b*b-c*c)<= ep)|(math.fabs(a*a+c*c-b*b)<= ep)|(math.fabs(c*c+b*b-a*a)<= ep)):
                        return "Tam giac vuong can"
                    else:
                        return "Tam giac can"
                else:
                    if((math.fabs(a*a+b*b-c*c)<= ep)|(math.fabs(a*a+c*c-b*b)<= ep)|(math.fabs(c*c+b*b-a*a)<= ep)):
                        return "Tam giac vuong"
                    else:
                        return "Tam giac thuong"
        else:
            return "Khong phai tam giac"


