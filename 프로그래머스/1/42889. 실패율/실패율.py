def solution(N, stages):
    answer = []
    dump = {}
    person = len(stages)
    # 각 스테이지별 실패율 계산
    for i in range(1, N+1):
        # 해당 스테이지에서 실패한 사람
        val = stages.count(i)
        if person == 0 :
            dump[i] = 0
        else:
            dump[i] = val / person
        person -= val
    # 실패율 내림차순 정렬, reverse = True(내림차순)
    answer = sorted(dump, key=lambda x:dump[x], reverse= True)
    
    return answer