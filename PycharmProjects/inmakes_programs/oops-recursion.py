num = 10
def f(num):
    n=10
    n1,n2=0,1
    n3 = n1 + n2
    n1 = n2
    n2 = n1
    return(f(num))
print(n3)


