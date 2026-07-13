def solution(keymap, targets):
    answer = []
    
    val = {}
    # 모든 keymap을 순회해서 값을 저장하기
    for keys in keymap:
        for i in range(len(keys)):
            # 문자
            char = keys[i]
            # 값
            count = i+1
            
            if char not in val:
                val[char] = count
            else:  # 이미 있으면 작은 값
                val[char] = min(val[char], count)
    for target in targets:
        total = 0
        for char in target:
            if char not in val:
                total = -1
                break
            total += val[char]
        answer.append(total)
    return answer