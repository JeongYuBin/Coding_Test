import sys
num = []

for i in range(9):
    a = int(sys.stdin.readline())
    num.append(a)

print(max(num))
print(num.index(max(num))+1)  # index 확인하는거 체크  