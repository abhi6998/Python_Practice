#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to swap alternate elements in the list.
def swapAlternate(arr):
    length = len(arr)
    for i in range(0, length-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


n = int(input())
arr = [int(i) for i in input().strip().split()[:n]]
swapAlternate(arr)
for i in arr:
    print(i, end=" ")
