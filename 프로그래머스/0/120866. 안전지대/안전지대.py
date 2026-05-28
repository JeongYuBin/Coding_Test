def solution(board):
    answer = 0
    n = len(board)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    danger = [[0]* n for _ in range(n) ]
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                danger[x][y] = 1
                for i in range(8):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0 <= nx <n and 0<= ny <n:
                        danger[nx][ny] = 1
                        
    # danger '0' 수 세기
    for x in range(n):
        for y in range(n):
            if danger[x][y] == 0:
                answer+=1 
        
    return answer   