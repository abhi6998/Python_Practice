#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find Sum of a list.
n = int(input())
sum = 0
list = [int(i) for i in input().strip().split()[:n]]
for i in list:
    sum += i
print(sum)
