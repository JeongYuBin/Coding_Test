def solution(s):
    answer = ''
    s = list(s)
    s = sorted(s)
    for i in s:
        if s.count(i) == 1:
            answer += i        
    
    return ''.join(answer)