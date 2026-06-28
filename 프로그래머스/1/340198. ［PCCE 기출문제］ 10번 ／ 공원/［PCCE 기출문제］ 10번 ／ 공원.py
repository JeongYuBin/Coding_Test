# mats를 내림차순으로 정렬
# 모든 칸을 시작점으로 사용

def solution(mats, park):
    answer = -1
    mats = sorted(mats, reverse=True)
    row = len(park)  # 행의 크기 
    col = len(park[0])  # 열의 크기
    
    for mat in mats:
        for i in range(row-mat+1):
            for j in range(col-mat+1):
                # mat x mat 검사
                flag = True
                for x in range(mat):
                    for y in range(mat):
                        if park[i+x][j+y] != "-1":
                            flag = False
                if flag:
                    return mat
    return answer