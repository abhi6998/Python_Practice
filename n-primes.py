#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find prime numbers in range specified by user using for loop.
# n = int(input())
# k = 2
# for k in range(2, n+1, 1):
#     flag = 0
#     for i in range(2, k, 1):
#         if k % i == 0:
#             flag = 1
#             break
#     if not(flag):
#         print(k)
# USING FUNCTIONS:
def isPrime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            break
    else:
        return True
    return False


def prime2ton(n):
    for i in range(2, n+1, 1):
        is_prime = isPrime(i)
        if is_prime:
            print(i)


prime2ton(10)
