# 물 먼저 먹으면 승리(물이 가운데 위치)
# 칼로리가 낮은 음식부터 배치
# 짝수개로 제공하기

def solution(food):
    answer = ''
    for i in range(len(food)):
        if i == 0:
            continue
        count = food[i] // 2
        for co in range(count):
            answer+= str(i)
            
    answer+= '0'
    k = len(answer)
    
    answer += answer[-2::-1]
        
    return answer