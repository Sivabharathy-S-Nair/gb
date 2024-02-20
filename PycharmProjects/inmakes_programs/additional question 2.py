def simple_interest(p,n,r):
    return (p*r*n)/100
p=int(input("Enter the pricipal amount,p:"))
r=int(input("Enter the rate,r:"))
n=int(input("Enter the n:"))
print(simple_interest(p,n,r))
