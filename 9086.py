import sys

T = int(sys.stdin.readline())

for i in range(T):
    # 문자열 맨 뒤에 \n 없애기 위해서 strip() 사용 필수!
    mun = sys.stdin.readline().strip()
    print(mun[0]+mun[-1])
