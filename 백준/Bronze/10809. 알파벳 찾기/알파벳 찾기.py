import sys

S = list(sys.stdin.readline().strip())
alp = [-1]*26

for i in range(len(S)):
    t = S[i] 
    val = ord(t)%97
    if alp[val] == -1:
        alp[val] = i
print(*alp)