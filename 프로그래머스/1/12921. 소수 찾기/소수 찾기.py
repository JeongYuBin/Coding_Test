def solution(n):
    answer = 0
    for i in range(2,n+1):
        value = 0 
        for k in range(2, int(i**0.5)+1):
            if i % k == 0:
                value = 1
                break
        if value == 0:
            answer += 1
            
    return answer