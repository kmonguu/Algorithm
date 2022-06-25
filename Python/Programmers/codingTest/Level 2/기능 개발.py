
#

# 다른 사람 풀이
# 100에서 현재 작업량을 뺀 남은 작업량에서 작업 속도를 나누어 남은 작업일수를 계산하는 방법

n = len(progresses)


finish_days = []
for i in range(n):
    remain = 100 - progresses[i]

    day = remain // speeds[i]
    if remain % speeds[i] != 0:
        day +=1

    finish_days.append(day)
