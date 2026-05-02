import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

a = 1 - a
b = 1 - b
c = 2 - c
d = 2 - d
e = 2 - e
f = 8 - f
print(a, b, c, d, e, f)