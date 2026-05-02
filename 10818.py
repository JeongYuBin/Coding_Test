import sys

num = int(sys.stdin.readline())
List = list(map(int, sys.stdin.readline().split()))
print(min(List), max(List))  # min, max 함수 사용 방식 확인