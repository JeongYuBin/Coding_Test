def solution(s):
    answer = True
    a, b = 0, 0
    for i in s:
        if i == "(":
            a += 1
        elif i == ")":
            b += 1
        
        if b > a:
            return False
    if a != b:
        return False
    
    return answer