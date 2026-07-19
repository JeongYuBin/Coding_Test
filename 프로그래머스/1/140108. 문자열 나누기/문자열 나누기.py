# 맨 처음 글자부터 확인한다
# 처음글자 b -> b와 같다 (같은 것 + 1)
# 두 번째 글자 a -> b와 다르다 (다른 것 + 1) 
# => 같은 것 개수 = 다른 것 개수 

def solution(s):
    answer = 0
    i = 0    # 현재 위치 
    
    while i < len(s):
        same = 0
        diff = 0
        word = s[i]
        
        for j in range(i, len(s)):
            if word == s[j]:
                same += 1
            else:
                diff +=1
            if same == diff:
                answer+= 1
                i = j+1  # 문자열을 잘랐으면 자른 시점부터 시작
                break
        else:
            answer += 1
            break
    return answer