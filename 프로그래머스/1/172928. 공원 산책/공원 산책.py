def solution(park, routes):
    # 시작 위치 
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j

    direction = {
        'N' : (-1, 0),
        'W' : (0, -1),
        'E' : (0, 1),
        'S' : (1, 0)
    }            
    
    # op, n 분리 및 이동 
    for ro in routes:
        op, n = ro.split(" ")
        n = int(n)
        
        dx, dy = direction[op]
        
        #현재 위치를 임시로 복사
        nx, ny = x, y
        # Flag
        possible = True
        # n만큼 진행
        for _ in range(n):
            nx += dx
            ny += dy
            # 공원 범위 밧아닌 경우 
            if nx < 0 or nx >= len(park):
                possible = False
                break
            if ny < 0 or ny >= len(park[0]):
                possible = False
                break
            if park[nx][ny] == 'X':
                possible = False
                break
        if possible:
            x, y = nx, ny
        
    return [x, y]