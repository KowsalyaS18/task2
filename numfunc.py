def my_func(list1,n):
    d=dict()
    for x in range(1,n+1):
        d[x]=x*x

    print(d)



list1=[]
n=int(input("enter the first list size"))
for i in range(0,n):
    item=int(input())
    list1.append(item)
print (list1)
my_func(list1,n)
