#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find Celsius of a temprature in fahrenheit.
def FtoC(start, end, skip):
    for i in range(start, end+1, skip):
        # C = (F-32) * 5/9
        celsius = (i - 32) * 5/9
        print(str(i)+"\t"+str(int(celsius)))


start = int(input())
end = int(input())
skip = int(input())
FtoC(start, end, skip)
