# 조합 수 : (각 종류별 의상 수 + 1)씩 해서 종류별 곱한 뒤, 1빼기(아무것도 입지 않는 경우)

def solution(clothes):
    answer = 0
    cloth = {}
    for i in range(len(clothes)):
        value, key = clothes[i][0], clothes[i][1]
        if key not in cloth:
            cloth[key] = []
            cloth[key].append(value)
        else:
            cloth[key].append(value)
    
    temp2 = 1
    for k in cloth:
        temp = len(cloth[k])
        temp2 *= (temp+1)
    
    answer = temp2 -1
    return answer