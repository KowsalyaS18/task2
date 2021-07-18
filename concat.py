list1=[]
n=int(input("enter the first list size"))
for i in range(0,n):
    item=int(input())
    list1.append(item)
print (list1)

list2=[]
n=int(input("enter the second list size"))
for i in range(0,n):
    item=int(input())
    list2.append(item)
print (list2)

list1=list1+list2
print(list1)
