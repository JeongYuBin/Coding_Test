import sys

T = int(sys.stdin.readline())

for i in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    # 문자열을 돌면서 문자열 안에 있는 문자 하나씩 횟수 곱하기 
    for ch in S:
        print(ch*R, end="")  # end = "" : 줄바꿈 없앰
    print()
    
    # result = ""
    # for ch in S:
    #     result += ch*R
    # print(result)