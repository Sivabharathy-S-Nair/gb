#x=lambda a:a+10
#print(x(2))
 #lambda in fun
def sample(a):
     return lambda x:a+x
ans=sample(2)
print(ans(3))
