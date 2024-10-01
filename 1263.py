# 진영이는 캠프 조교를 온 후 효율적으로 시간 관리를 해야 한다는 것을 깨달았다. 진영이는 하루에 해야 할 일이 총 N개가 있고 이 일들을 편하게 1번부터 N번까지 차례대로 번호를 붙였다.

# 진영이는 시간을 효율적으로 관리하기 위해, 할 일들에 대해 끝내야할 시간과 걸리는 시간을 적은 명단을 만들었다. 즉, 이 명단은 i번째 일은 일을 처리하는데 정확히 Ti 시간이 걸리고 Si 시 내에 이 일을 처리하여야 한다는 것을 담고 있다. 진영이는 0시부터 활동을 시작할 수 있고, 두 개 이상의 일을 같은 시간에 처리할 수 없다.

# 진영이가 바라는 점은 최대한 늦잠을 자는 것이다. 문제는 이러한 진영이를 도와 일들은 모두 마감시간 내에 처리할 수 있는 범위 내에서 최대한 늦게 일을 시작할 수 있는 시간이 몇 시인지 알아내는 것이다.

# 입력
# 첫째 줄에 일의 수 N이 입력되고 다음 N개의 줄에 대해 i+1번째 줄에는 i번째 일에 대한 Ti와 Si가 입력된다.

# 진영이가 일을 모두 끝마칠 수 있는 가장 늦은 시간을 출력한다. 만약 0시부터 시작하여도 일을 끝마칠 수 없다면 -1을 출력한다.

#######################
# 초기 코드 (리스트에 저장이 되지 않고 마지막만 출력되는 오류)

# N = int(input())
# for i in range(N):
#     work = list(map(int, input().split()))

# print(work) -> 마지막 입력한 값만 출력

#######################
N = int(input())
work = []   # 모든 입력을 저장할 리스트
play = 0


for i in range(N):
    t, s = map(int, input().split())  # 입력받은 값을 임시 리스트에 저장
    work.append((t, s))   # 각 입력을 work 리스트에 추가

first_hap = sum(w[0] for w in work)   # w[0]는 for문의 w 이다
max_second = max(w[1] for w in work)  # 두 번째 값들 중에서 가장 큰 값을 찾음
work = sorted(work, key=lambda x: x[1]) # 각 리스트의 두 번째 값을 기준으로 오름차순 정렬

# sorted(work, key=lambda x: x[1]): 각 리스트의 두 번째 값(x[1])을 기준으로 work 리스트를 정렬합니다. lambda x: x[1]은 각 리스트에서 두 번째 값을 반환하는 익명 함수이다.

flag = True

if first_hap > max_second:
    play = 1
    flag = False

while flag:
    time = play
    for i in range(len(work)):
        if work[i][0] + time <= work[i][1] :
            time += work[i][0]
        else:
            flag = False
            break
    if flag:
	    play += 1
    

print(play - 1)
