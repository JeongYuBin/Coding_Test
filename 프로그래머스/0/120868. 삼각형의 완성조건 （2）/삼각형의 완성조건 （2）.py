def solution(sides):
    answer = 0
    a = sides[0]
    b = sides[1]
    c = max(a,b)
    d = min(a,b)
    # c-d < x <= c
    # c-d+1 <= x <= c
    for i in range(c-d+1, c+1):
        answer += 1
    for i in range(c+1, c+d):
        answer += 1
    
    return answer