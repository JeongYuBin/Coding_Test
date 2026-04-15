import sys

# sys.stdin.readline()
# 맨 끝에 개행문자(\n)까지 같이 입력 받음 .rstrip() 
num = int(sys.stdin.readline())
# num = int(sys.sdin.readline().rstrip())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)