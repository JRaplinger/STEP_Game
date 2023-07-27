n=int(input("enter the range: "))
k=int(input("enter the iterations: "))
a= pow(2,k)
b=n/a
c=n-b
print("Eliminated: " + str(c))
print("remaining: " + str(b))