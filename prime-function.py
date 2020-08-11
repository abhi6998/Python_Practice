#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find prime number using functions.
# basic solution
#  METHORD 1 : NOT OPTIMISED
# def isPrime(n):
#     flag=0
#     for i in range(2,n,1):
#         if n%i==0:
#             flag=1
#             break
#     if flag==1:
#         return("Number is not prime")
#     else:
#         return("Prime")
#
# isPrime(3)

# METHORD 2 : OPTIMISED

def isPrime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            break
    else:
        return True
    return False
