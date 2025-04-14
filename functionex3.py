def sumop():
    k=int(input("enter the value:"))
    v=int(input("enter the value:"))
    c=k+v
    return k,v,c
x,y,res=sumop()
print("sum({}+{})={}".format(x,y,res))
print("*"*50)
hyd=sumop()
print(hyd,type(hyd))
print("sum({}+{})={}".format(hyd[0],hyd[1],hyd[2]))
