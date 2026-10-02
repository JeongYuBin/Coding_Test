# 장르별 -> 장르 내에서 많이 재생된 노래 (장르별 최대 2개씩)

def solution(genres, plays):
    answer = []
    diction = {}
    for i in range(len(genres)):
        key, value = genres[i], plays[i]
        if key not in diction:
            diction[key] = value
        else:
            temp = diction[key]
            diction[key] = value + temp
    # diction 내림차순, value 기준 -> 리스트로 변경됨
    diction = sorted(diction.items(), key=lambda x:x[1], reverse=True)
    
    # 재생 수와 인덱스를 하나로 묶기 
    for key, total in diction:
        award = []
        for j in range(len(genres)):
            if genres[j] == key:
                award.append([plays[j], j])
        # award 정렬
        award.sort(key=lambda x:(-x[0], x[1]))
        
        # 각 장르마다 2개씩 넣기 
        for awa in award[:2]:
            answer.append(awa[1])
            
    return answer
