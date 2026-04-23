import sys

N = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().strip()))
result = 0

for i in range(N):
    result += M[i]

print(result)