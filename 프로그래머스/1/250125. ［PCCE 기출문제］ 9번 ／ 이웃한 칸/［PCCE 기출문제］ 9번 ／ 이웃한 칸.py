def solution(board, h, w):
    answer = 0
    dh = [0, 1, -1, 0] # 행
    dw = [1, 0, 0, -1]  # 열 
    
    for i in range(4):
        if h+dh[i] >= 0 and h+dh[i] < len(board):
            if w+dw[i] >= 0 and w+dw[i] < len(board[0]):
                if board[h+dh[i]][w+dw[i]] == board[h][w]:
                    answer +=1 
    return answer