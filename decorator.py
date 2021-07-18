def dec(func):
    def inner(*args):
        digits = []
        for i in args[0]:
            if str(i).isdigit():
                digits.append(i)
        return func(digits)
    return inner

@dec
def sumofele(l):
    s=0
    for i in l:
        s+=i
    return s 

print(sumofele([1,2,3,4,5,'a','b'])) 
