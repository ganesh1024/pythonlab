
#num = int(input("Enter a number: "))

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")
#
## prime number in function
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


