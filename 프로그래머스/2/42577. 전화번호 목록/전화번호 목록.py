# 접두어가 있으면 false, 없으면 true
# 정렬을 한 뒤, 바로 앞 번호끼리 비교하기 -> 정렬을 하면 같은 접두어를 가진 문자열끼리 모임
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        check = phone_book[i-1]
        val = phone_book[i]
        if val[:len(check)] == check:
            answer = False
            break
    
    return answer