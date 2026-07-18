# 값을 len(p) 만큼 나누고 해당 값을 p 와 비교

def solution(t, p):
    answer = 0 
    for i in range(len(t)-len(p)+1):
        value = t[0+i:len(p)+i]
        if int(value) <= int(p):
            answer += 1
    return answer