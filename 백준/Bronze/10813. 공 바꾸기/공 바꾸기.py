import sys

N, M = map(int, sys.stdin.readline().split())
# 각 바구니 번호에 맞는 값을 초기값으로 가지기 
basket = list(range(1, N+1))     

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

print(*basket)