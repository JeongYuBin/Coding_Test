def solution(nums):
    answer = 0
    dump = list(set(nums))
    if len(dump) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(dump)