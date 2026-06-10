# 말할 수 있는 언어를 빈문자열로 replace 한다
# for문을 모두 돌렸을때, 빈문자열 개수가 말할 수 있는 단어이다
def solution(babbling):
    answer = 0
    word = ["aya","ye", "woo", "ma"]
    for b in babbling:
        for w in word:
            b = b.replace(w, " ")
        if b.strip() == "":
            answer+=1
    return answer
