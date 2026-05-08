def solution(hp):
    general_ant = hp // 5
    byong_ant = hp % 5 // 3
    il_ant = hp % 5 % 3 
    answer = general_ant + byong_ant + il_ant
    return answer