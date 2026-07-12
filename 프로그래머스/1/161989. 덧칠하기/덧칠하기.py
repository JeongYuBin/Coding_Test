def solution(n, m, section):
    answer = 0
    paint = 0 
    for sec in section:
        if sec > paint:
            paint =  sec + m - 1
            answer +=1 
                
    return answer