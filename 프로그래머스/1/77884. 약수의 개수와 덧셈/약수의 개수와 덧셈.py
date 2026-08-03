def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        for j in range(1, int(i**(1/2))+1):
            value = 0 
            if i % j == 0:
                if i // j == j:
                    value += 1
                else:
                    value += 2
        if value % 2 == 0:
            answer += i
        else:
            answer -= i
        
    return answer