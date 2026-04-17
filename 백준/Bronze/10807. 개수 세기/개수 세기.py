import sys

N = int(sys.stdin.readline()) 
L = list(map(int, sys.stdin.readline().split()))  # List로 전달
check = int(sys.stdin.readline())
print(L.count(check))  # L(list)에서 check가 몇 개 있는지 