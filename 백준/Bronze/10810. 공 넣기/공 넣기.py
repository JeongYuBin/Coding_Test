import sys

# N개 바구니
# M은 횟수
# 바구니 안에는 1~N의 숫자가 적힌 공
# 가장 처음 바구니에는 공 없음, 1개만 넣을 수 있음
# 각 바구니에 어떤 번호가 있는지 없으면 0 

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N

for _ in range(M):
    # i번 바구니부터 j번 바구니까지 k번 번호가 적혀있는 공을 넣는다.
    i, j, k = map(int, sys.stdin.readline().split())  
    for t in range(i-1, j):  # i-1, j-1까지
        basket[t] = k
# 최종적으로 각 바구니에 어떤 공이 들어있는지
print(*basket)    
