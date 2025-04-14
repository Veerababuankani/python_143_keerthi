#FunSumAvgEx1.py
def readvalues():
    lst=[]
    n=int(input("enter how many values u want:"))
    if n<=0:
        return lst
    else:
        for i in range(1,n+1):
            val=int(input("enter the {} val one by one:".format(i)))
            lst.append(val)
        return (lst)
def SumAndAvg(kvrlst):
    if (len(kvrlst)<0):
        print("list is empty can't find the avg and sum")
    else:
        #find the sum and avg
        s=0
        for val in kvrlst:
            s=s+val
        else:
            print("given list of elements:{}".format(kvrlst))
            print("sum of {}".format(s))
            print("avg:{}".format(s/len(kvrlst)))

#main program
lst=readvalues()
SumAndAvg(lst)