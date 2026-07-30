# k번 이상 신고 당하면 정지
# 정지 당할경우 해당 사용자를 신고한 사용자 모두에게 메일 송부
# 신고한 사람 : 신고 당한 사람

# diction1 {신고 받은 사람 아이디 : 받은 횟수}
# diction2 {신고 받은 사람 아이디 : (신고한 사람)}
# 받은 횟수가 k 이상인 key값을 가져와서 해당 key 값을 통해서 diction2에서 신고한 사람마다 +1
# +1은 id_list의 index를 확인해서 result의 해당 index 값에 +1 하기


def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dictions = {}
    
    for i in range(len(report)):
        reporter, reported = report[i].split(' ')
        if reported not in dictions:
            dictions[reported] = set()
        dictions[reported].add(reporter)
    
    for reported in dictions:
        if len(dictions[reported]) >= k:
            for reporter in dictions[reported]:
                index = id_list.index(reporter)
                answer[index] +=1
                
        
    return answer