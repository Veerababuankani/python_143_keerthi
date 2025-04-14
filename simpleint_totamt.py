#simpleint_totamt.py
def simleint():
    p=float(input("enter the value of principle amt:"))
    t=float(input("enter the value of principle time:"))
    r=float(input("enter the value of rate of insterst:"))
    #cal the simpleint
    si=p*t*r/100
    tolamt=p+si
    return p,t,r,si,tolamt
#main program
res=simleint()
print("*"*100)
print("\t simple insterst calculations")
print("*"*100)
print("principle amount:{}".format(res[0]))
print("principle time:{}".format(res[1]))
print("rate of insterst:{}".format(res[2]))
print("simple insertest:{}".format(res[3]))
print("total amount:{}".format(res[4]))
print("*"*100)