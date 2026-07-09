def solution(a, b):
    answer = 0
    a, b = str(a), str(b)
    
    hap = a+b
    plus = b+a
    hap = int(hap)
    plus = int(plus)
    
    if hap > plus : 
        answer = hap
    else: 
        answer = plus
    
    return answer