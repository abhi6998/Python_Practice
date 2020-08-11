#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find prime number using for while loop
range_end = int(input())
prime_number = 2
while prime_number <= range_end:
    flag = False
    divisor = 2
    while divisor < prime_number:
        if prime_number % divisor == 0:
            flag = True
        divisor += 1
    if not(flag):
        print(prime_number)
    prime_number += 1
    pass
