n = int(input("enter the n value"))
fact = 1
if n == 0 | n == 1:
    print("The factorial of a number is ",n)
else:

    for i in range(2,n+1):
        fact = fact * i

    print("the factorial of num ",n ,"is",fact)

