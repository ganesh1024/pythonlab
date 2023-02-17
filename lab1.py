a = int(input('enter the number'))
b = int(input('enter the number'))
c = a + b
print(c)

##fibonacci
# fibonacci

# n = int(input('enter the n value'))
# a = 0
# b = 1
# temp = 0
#
# if n <= 0:
#     print('please enter  correct value')
#
# elif n == 1:
#     print("fibo sequence :", n)
#
# else:
#     print("sequence:")
#     while temp < n:
#         print(a)
#         c = a + b
#         a = b
#         b = c
#         temp += 1

##fibonaci with function

n = int(input('enter the n value'))
def fibo(n):
    a = 0
    b = 1
    temp = 0

    if n <= 0:
        print('please enter  correct value')

    elif n == 1:
        print("fibo sequence :", n)

    else:
        print("sequence:")
        while temp < n:
            print(a)
            c = a + b
            a = b
            b = c
            temp += 1

fibo(n)

prime

num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")

# prime number in function
n = int(input("Enter a number: "))
def prime(num):
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")

prime(n)


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







