#Print aseibonacci sequence is the integer sequence  0, 1, 1, 2, 3, 5, 8, 13,
#21, 34, 55, 89, 144
def fibo(x):
    if x<=1:
        return x
    else:
        return fibo(x-1)+fibo(x-2)
for i in range(13):
    print(fibo(i),end=" ")

