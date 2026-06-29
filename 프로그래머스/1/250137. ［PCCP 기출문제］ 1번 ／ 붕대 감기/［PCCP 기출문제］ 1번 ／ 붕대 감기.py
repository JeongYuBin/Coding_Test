# 1초마다 x 체력 회복, t초동안 하면 t*x + y 회복
# 이전 공격이후부터 이번 공격 직전 까지의 회복 시간을 구해야 한다
# 기본 회복 = 회복 가능 시간 * 초당 회복량
# 추가 회복 = (회복 가능 시간 // 시전 시간) * 추가 회복량 
# 현재 체력 = min(health, 현재 체력 + 기본 회복 + 추가회복)
# 공격 받을 경우, 현재 체력 -= 피해량 
# 죽으면 바로 -1
# 마지막 공격 시간 갱신, 마지막 공격시간= 공격 시간 

def solution(bandage, health, attacks):
    now_health = health
    prev_time = 0  # 현재 시간 
    
    for time, damage in attacks:
        heal_time = time - prev_time - 1
        
        # 기본 회복
        heal = heal_time * bandage[1]
        # 추가 회복
        plus_heal = (heal_time // bandage[0]) * bandage[2]
        # 공격 직전까지 회복
        now_health = min(health, now_health+heal+plus_heal)
        # 공격 받기
        now_health -= damage
        if now_health <= 0:
            return -1
        
        prev_time = time
    return now_health