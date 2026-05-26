def solution(dots):
    answer = 0
    x = []
    y = []
    
    for i in range(len(dots)):
        x.append(dots[i][0])
        y.append(dots[i][1])
    x = max(x) - min(x)
    y = max(y) - min(y)
    answer = x*y    
    
    return answer