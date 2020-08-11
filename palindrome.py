# Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find Palindrome of a number.
print("Enter the number to check if palindrome or not")
input_number = int(input())
original_number = input_number
reverse_number = 0
while input_number > 0:
    reminder = input_number % 10
    reverse_number = (reverse_number*10) + reminder
    input_number = input_number // 10
if (original_number==reverse_number):
    print(original_number,"is a palindrome")
else:
    print(original_number,"is not a palindrome")

#using functions
# def isPalindrome(n):
#     original_num = n
#     reverse = 0
#     while(n > 0):
#         rem = n % 10
#         reverse = (reverse*10) + rem
#         n = n//10

#     if reverse == original_num:
#         return("true")
#     else:
#         return("false")


# n = int(input())
# isPalindrome(n)
