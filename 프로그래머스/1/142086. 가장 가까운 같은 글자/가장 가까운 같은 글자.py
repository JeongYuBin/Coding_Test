# 한 글자씩 마다 저장을 해서 딕셔너리에 넣기
# 그리고 하나씩 갈 때마다 딕셔너리 값을 1씩 업데이트

def solution(s):
    answer = []
    diction = {}
    for i in range(len(s)):
        if s[i] not in diction:
            diction[s[i]] = 0
            answer.append(-1)
        elif s[i] in diction:
            answer.append(diction[s[i]])
            diction[s[i]] = 0 
        for j in diction:
            diction[j] += 1
            
    return answer