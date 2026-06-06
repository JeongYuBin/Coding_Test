def solution(lines):
    answer = 0
    count = [0]*201
    for start, end in lines :
        for i in range(start, end):
            count[i+100] += 1  # 가운데 
    
    # 배열 세기
    for c in count:
        if c >= 2:
            answer += 1
    
    return answer