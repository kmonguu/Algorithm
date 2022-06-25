# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지 반환

# 내가 푼 코드
# progresses와 speeds를 deque로 만들고,
# 각 작업의 진도에 개발 속도를 더해가면서 해당 작업이 100%가 되었을 때 큐에서 pop하면서 같이 배포할 수 있는 기능의 수를 구해줌

# deque를 사용하면서 발생한 typeerror: object of type set is not json serializable
# json 모듈이 해당 오브젝트를 제대로 인식하지 못하는 문제로, progresses와 speeds를 deque로 정의하는 과정에
# progresses = deque(progresses)를 list로 타입을 정의해주어 progresses = deque(list(progresses))로 해결할 수 있었다.

from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(list(progresses))
    speeds = deque(list(speeds))
    
    while progresses:
        for idx in range(len(progresses)):
            progresses[idx] += speeds[idx]
        
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

    
    return answer

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
