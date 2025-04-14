#multable.py
def multab(n):
    print("*" * 50)
    if(n<=0):
        print("its is invalid input--->({})".format(n))
        print("*" * 50)
    else:
        for i in range(1,11):
            print("{} X {} = {}".format(n,i,n*i))
        print("*"*50)
#main program
n=int(input("enter the muliplication table:"))
multab(n)