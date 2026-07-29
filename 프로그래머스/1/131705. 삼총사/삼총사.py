# 모든 값의 순서쌍 만큼 더하고 나서 3개씩 묶어서 더해
# 그리고 해당 값이 0이면 answer += 1

def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if number[i]+number[j]+number[k] ==0:
                    answer+=1
    return answer