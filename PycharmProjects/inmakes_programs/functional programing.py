def addition(a,b):
    return a+b
def square(c):
    return c*c
#result=square(addition(2,9))
a=int(input("enter a number:"))
b=int(input("enter a number:"))
result=square(addition(a,b))

print(result)
