#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find Amstrong of a number
def isAmstrong(n):
    original_num = n
    palin = 0
    length = len(str(n))
    while n > 0:
        rem = n % 10
        rem = rem**length
        palin = rem + palin
        n = n//10
    if original_num == palin:
        print("true")
    else:
        print("false")


n = int(input())
isAmstrong(n)
