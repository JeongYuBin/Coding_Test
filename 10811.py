import sys
# 슬라이싱(slicing) 사용

N, M = map(int, sys.stdin.readline().split())
basket = list(range(1, N+1))

for k in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1: j] = basket[i-1:j][::-1]

print(*basket)

