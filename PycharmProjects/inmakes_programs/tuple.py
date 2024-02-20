x=(1,2,"table",)
print(type(x))
print(x[0])
print(x)
y=list(x)
print(type(y))
y.insert(1,"ee")
print(y)
x=tuple(y)
print(x)


#partt 2
x=(2,3,"hi","k")
print(len(x))
y=tuple(("hi",7,8))
print(y)
for k in y:
    print(k)
x=(1,2,3,3)
#y=(7,9,"uu")
#print(x+y)
y=x*3
print(y)
