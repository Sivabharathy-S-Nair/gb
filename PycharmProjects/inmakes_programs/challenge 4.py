#Write a function which would divide two numbers, design thefunction in a manner that it handles
# the divide by zero exception
def division(a,b):
  try:
      return a/b
  except:
         print("There is a divison error.")
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(division(a,b))
