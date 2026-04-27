import sys

a = list(sys.stdin.readline().strip())
result = 1

for i in range(len(a)):
    if a[i] != a[-(i+1)]:
        result = 0
        break
print(result)
