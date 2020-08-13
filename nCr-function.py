#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find ncr using recursion.
def fact(n):
    n_fact = 1
    for i in range(1, n+1):
        n_fact *= i
    return n_fact


def ncr_func(n, r):
    ncr = fact(n)//(fact(r)*fact(n-r))
    return ncr


n = int(input())
r = int(input())


print(ncr_func(n, r))
