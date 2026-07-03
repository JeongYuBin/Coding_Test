# n : 상자 개수 
# w : 가로 길이
# num : 꺼내려는 상자

def solution(n, w, num):
    answer = 1 # 본인 포함
    idx = num - 1
    row = idx // w
    col = idx % w
    
    if row % 2 == 1:
        col = w - 1 - col
    
    for box in range(num+1, n+1):
        box = box - 1
        box_row = box // w
        box_col = box % w
        
        if box_row % 2 == 1:
            box_col = w - box_col - 1 
        
        if box_col == col:
            answer += 1
     
    return answer