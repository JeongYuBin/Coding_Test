import sys

num = int(sys.stdin.readline())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {a+b}")
    # print("Case #"+str(i+1)+": "+str(a+b))