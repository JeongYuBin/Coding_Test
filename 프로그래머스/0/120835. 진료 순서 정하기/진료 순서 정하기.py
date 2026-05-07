def solution(emergency):
    answer = []

    # 큰 숫자부터 정렬
    rank = sorted(emergency, reverse=True)
    # [30, 10, 23, 6, 100] 일때,
    # sorted 진행 -> rank: [100, 30, 23, 10, 6]
    

    # 원래 배열 순회
    for i in emergency:
        # 정렬된 배열에서 몇 번째 위치인지 찾기
        # i는 기존 배열의 값
        answer.append(rank.index(i) + 1)

    return answer