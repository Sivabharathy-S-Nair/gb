#3.Create a tuple with 7 elements
#1. Use Insert, Append.
#2. Print the last second element.
colours=("black","brown","red","violet","purple","orange","blue")
x=list(colours)
x.insert(1,"yellow")
print(x)
x.append("green")
print(x)
colours=tuple(x)
print(colours)
print(colours[-2])
