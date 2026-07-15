# s의 각 알파벳을 index 만큼 뒤의 알파벳으로 변경
# skip 에 있는 알파벳은 제외 

# 한 글자씩 index 만큼 진행하는데, 해당 글자가 in skip 에 포함되면 continue 
# 글자들을 아스키 코드만큼 진행? a: 97~122, A: 65

def solution(s, skip, index):
    answer = ''
    
    for i in range(len(s)):
        val = ord(s[i])  # 현재 문자의 아스키 코드
        for j in range(index):
            val += 1 # 한 칸 이동
            if val > 122:
                val -= 26
            # 이동한 문자가 skip에 있으면 계속 다음 문자로 이동
            while chr(val) in skip: 
                val += 1
                if val > 122:
                    val -= 26
        ch = chr(val)
        answer += ch
    
    return answer