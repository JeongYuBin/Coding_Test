import sys

student = [0]*31  # 인덱스 1 ~ 30 만 사용

for i in range(28):
    num = int(sys.stdin.readline())
    student[num] = 1  # 학생이 있는 곳의 값 '1'

for i in range(1, 31):
    if student[i] == 0:
        print(i)