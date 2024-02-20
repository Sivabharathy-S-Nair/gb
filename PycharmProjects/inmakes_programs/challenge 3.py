
def final_price(x,y):

#Final Price(FP) = (ProductPriceofX)/(ProductPriceofY)^2.
    return (x)/(y)**2

x=int(input("Enter the product price of X"))
y=int(input("Enter the product price of Y"))
print(final_price(x,y))
