#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find reverse of a list.
def reverse_l(arr):
    arr = arr[-1:-n-1:-1]
    return (arr)


n = int(input("size"))
arr = [int(i) for i in input("array").strip().split()[:n]]
reverse_l(arr)

# OR


# def reverse_l(arr):
#     length = len(arr)
#     for i in range(length//2):
#         arr[i], arr[length-i-1] = arr[length-i-1], arr[i]
#
#
# n = int(input("size"))
# arr = [int(i) for i in input("array").strip().split()[:n]]
# reverse_l(arr)
# print(arr)
