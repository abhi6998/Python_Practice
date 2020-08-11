#Author - Abhishek Shah
#Github - Abhi6998
#This program is part of python Practice.
#Program to find fibonacci series till the number specified.
range_end = int(input())
f1 = 0
f2 = 1
fn = 0
i = 0
print("the fibonaci series is:")
print(f1)
print(f2)
while i <= range_end:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    if fn <= range_end:
        print(fn)
    i += 1
