# 가로와 세로중 긴 변을 찾아 -> 각 배열의 w,h중 작은 것들 중의 큰 것 찾기

def solution(sizes):
    answer = 0
    w = 0
    h = 0 
    for i in range(len(sizes)):
        if w == 0:
            w = sizes[i][0]
        else:
            if w > sizes[i][0]:
                continue
            else:
                w = sizes[i][0]
    for j in range(len(sizes)):
        if h == 0:
            h = sizes[j][1]
        else:
            if h > sizes[j][1]:
                continue
            else:
                h = sizes[j][1]   
    max_value = max(w, h)
    
    # 각 배열의 w와 h 비교하기 
    check = 0
    for k in range(len(sizes)):
        if check == 0:
            check = min(sizes[k][0], sizes[k][1])
        else:
            min_value = min(sizes[k][0], sizes[k][1])
            check = max(check, min_value)
            
    answer = max_value * check
    
    return answer