import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
count = 0
M = max(L)

for i in range(N):
    value = L[i]
    L[i] = value/M*100
    count += L[i]
print(count/N)
