#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find Duplicate element in a list.
def duplicate(arr, n):
    res = 0
    for i in range(n):
        res = res ^ arr[i]
        res = res ^ i
    return res


n = int(input())
arr = [int(i) for i in input().strip().split()[:n]]
duplicate(arr, n)

# n = int(input())
# arr = [int(i) for i in input().strip().split()[:n]]
# for i in range(n):
#     for j in range(n):
#         if i!=j and arr[i] == arr[j]:
#             ans = arr[i]
#         else:
#             continue
# print(ans)
