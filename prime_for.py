#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find prime number using for loop
# basic solution
n = int(input())
prime = 2
flag = False
for i in range(prime, n, 1):
    if n % prime == 0:
        flag = True
        break
if flag:
    print(" not prime")
else:
    print("prime")

#optimised solution : 
# n = int(input())
# for i in range(2, n, 1):
#     if n % i == 0:
#         break
# else:
#     print("prime")