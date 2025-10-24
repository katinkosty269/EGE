from math import *

a = int(input())
b = int(input())
c = int(input())

p = (a+b+c)/2
s = int(sqrt(p*(p-a)*(p-b)*(p-c)))
print(int(s))