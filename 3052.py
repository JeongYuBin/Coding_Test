import sys

# 서로가 모두 다르다는 것을 확인하는 방법
# Python 에서는 set 함수가 있다

remain = [0]*10
for i in range(10):
    num = int(sys.stdin.readline())
    remain[i] = num%42

# 중복 제거
print(len(set(remain)))

# set 함수를 사용하지 않고 해결 방법
# unique = []

# for x in remain:
#     if x not in unique: # 처음 나온 값이면(해당 값이 새로운 배열에 없다면)
#         unique.append(x)  # 해당 배열에 추가하기 
# print(len(unique))
