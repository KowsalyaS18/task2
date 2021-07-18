def remove(list1):
    x=int(input("enter an element to remove"))
    list1.remove(x)
    return(list1)
    
def add_element(list1):
    x=int(input("enter an element to add"))
    y=int(input("enter the position to add"))
    list1.insert(y,x)
    return(list1)
    

list1=[]
n=int(input("enter the list size"))
for i in range(0,n):
    item=int(input())
    list1.append(item)
print(list1)

print(remove(list1))

print(add_element(list1))
