#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find odd and even numbers in a list's sum.
input_number = int(input())
even_number_sum = 0
odd_number_sum = 0
while input_number > 0:
    part_of_number = input_number % 10
    input_number = input_number // 10
    if part_of_number % 2 == 0:
        even_number_sum += part_of_number
    else:
        odd_number_sum += part_of_number
print("even_number_sum = ",even_number_sum,"\t odd_number_sum =",odd_number_sum)
