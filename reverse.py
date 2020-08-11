#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find reverse of a number
print("enter the number to reverse it")
input_number = int(input())
reverse_number = 0
while input_number > 0:
    reminder = input_number % 10
    reverse_number = (reverse_number * 10) + reminder
    input_number = input_number // 10
print(f"The reversed number is \n{reverse_number}")
