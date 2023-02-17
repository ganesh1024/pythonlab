n = int(input("enter the number"))
sum1 = 0
temp = n

    while temp>0:
        num=temp % 10
        sum1 += num**3
        temp = temp // 10

if n == sum1:
    print("Given number",n," is a armstrong number")
else:
    print("Given Number",n," is not a armstrong number")







