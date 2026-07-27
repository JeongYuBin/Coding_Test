# 문자를 하나 선택해서 if i in diction 

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for babb in babbling:
        previous = ''
        for word in words:
            if word in babb:
                # 같은 단어 나오면 실패
                if word*2 in babb:
                    break
                previous = word
                babb = babb.replace(word, ' ')
                babb = babb.strip()
        if babb == '':
            answer += 1
                
    return answer