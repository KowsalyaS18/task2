def my_func(list1):
    print(sum(list1))



list1=[]
n=int(input("enter the  list size"))
for i in range(0,n):
    item=int(input())
    list1.append(item)
print (list1)

my_func(list1)
