def solution(park, routes):
    # 시작 위치 확인
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j
    # 방향 설정
    direction = {
        'N': (-1, 0),
        'E': (0, 1),
        'W': (0, -1),
        'S': (1, 0)
    }
    # 방향 수정
    for route in routes:
        dire, val = route.split(" ")
        val = int(val)
        dx, dy = direction[dire]
        # 현재 위치를 변경하지 않고 임시 위치 생성
        nx, ny = x, y
        
        for _ in range(val):
            nx += dx
            ny += dy
            # 범위를 벗어난 경우
            if nx < 0 or nx >= len(park):
                break
            if ny < 0 or ny >= len(park[0]):
                break
            # 장애물을 만나는 경우
            if park[nx][ny] == 'X':
                break
        else:
            x, y = nx, ny
                
    return [x,y]
    
    
# def solution(park, routes):
#     # 시작 위치 
#     for i in range(len(park)):
#         for j in range(len(park[0])):
#             if park[i][j] == 'S':
#                 x, y = i, j

#     direction = {
#         'N' : (-1, 0),
#         'W' : (0, -1),
#         'E' : (0, 1),
#         'S' : (1, 0)
#     }            
    
#     # op, n 분리 및 이동 
#     for ro in routes:
#         op, n = ro.split(" ")
#         n = int(n)
        
#         dx, dy = direction[op]
        
#         #현재 위치를 임시로 복사
#         nx, ny = x, y
#         # Flag
#         possible = True
#         # n만큼 진행
#         for _ in range(n):
#             nx += dx
#             ny += dy
#             # 공원 범위 밧아닌 경우 
#             if nx < 0 or nx >= len(park):
#                 possible = False
#                 break
#             if ny < 0 or ny >= len(park[0]):
#                 possible = False
#                 break
#             if park[nx][ny] == 'X':
#                 possible = False
#                 break
#         if possible:
#             x, y = nx, ny
        
#     return [x, y]