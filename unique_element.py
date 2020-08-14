#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find Unique element in a list.
# METHORD 1 - VERY BAD SOLUTION DUE TO VERY BIG TIME COMPLEXITY
# def FindUnique(arr, n):
#     for i in range(n):
#         for j in range(n):
#             if i != j and arr[i] == arr[j]:
#                 break  # if this break is exedcuted the else part in the next line
#                 # wont be executed as the entire for loop will be terminated
#         else:
#             print(arr[i])
#
#
# n = int(input("size of array"))
# arr = [int(i) for i in input("enter the array").strip().split()[:n]]
# FindUnique(arr, n)

# METHORD 2 - ONLY WORKS IF THE REPEATED NUMBERS ARE IN PAIRS


def find(ar, n):

    res = ar[0]

    for i in range(1, n):
        res = res ^ ar[i]

    return res


n = int(input())
ar = list(int(i) for i in input().strip().split(' '))
print(find(ar, len(ar)))
