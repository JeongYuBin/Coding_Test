SELECT round(sum(ifnull(length, 10))/count(*), 2) as AVERAGE_LENGTH
FROM FISH_INFO