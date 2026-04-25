import sys

a, b = list(sys.stdin.readline().split())
a = a[::-1]
b = b[::-1]

if a > b :
    print(a)
else: 
    print(b)