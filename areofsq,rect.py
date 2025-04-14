def areaofrecangle():
    l=float(input("enter the length:"))
    b=float(input("enter the breadth:"))
    if l<0 or b<0:
        print("invalid")
    else:
        area1=l*b
        print("area of rectangle is {}X{}={}".format(l,b,area1))
def ardeaofsq():
    s=float(input("enter the side of square:"))
    if s<0:
        print("invalid")
    else:
        area2=s*s
        print("area of square is {}X{}={}".format(s, s, area2))

#main program
areaofrecangle()
ardeaofsq()
