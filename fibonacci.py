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
