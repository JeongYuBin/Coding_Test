# 명단에 k만큼 들어가는 배열이 있어야 함
# 해당 배열에 값을 넣는 대신에 오름차순 정렬하기 맨 첫번째 값이 가장 작은 값
# answer에는 명예 값의 0번째 넣기
# 오름차순 : .sort()

def solution(k, score):
    answer = []
    honor = []
    for sc in score:
        if len(honor) < k:
            honor.append(sc)
            honor.sort()
            answer.append(honor[0])
        elif len(honor) >= k:
            if honor[0] >= sc:
                answer.append(honor[0])
            else:
                honor[0] = sc
                honor.sort()
                answer.append(honor[0])
        
    return answer