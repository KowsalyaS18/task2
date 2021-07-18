def my_func(list1):
    
    unique = []
    for a in list1:
        if a not in unique:
            unique.append(a)
    return unique
  
list1=[]
n=int(input("enter the  list size"))
for i in range(0,n):
    item=int(input())
    list1.append(item)
print (list1)

print(my_func(list1))
