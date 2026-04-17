import sys

a, b = map(int, sys.stdin.readline().split())
List = list(map(int, sys.stdin.readline().split()))

small_value = [x for x in List if x < b]
"""
x for x in List if x < b

for x in List
    if x < b 
        small_value.append(x)

"""

print(*small_value)  # *를 사용하면 리스트를 하나씩 풀어줌
# print(small_value)를 하면 [1, 4, 2 ,3] 으로 출력