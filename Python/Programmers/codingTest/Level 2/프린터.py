# 중요도가 높은 문서를 먼저 출력하는 프린터의 동작방식은 아래와 같은 방식으로 동작합니다.
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# 내가 푼 코드 (queue 사용)
# 매개변수로 들어오는 arr과 그 인덱스를 담는 idx 배열을 deque로 선언
# arr의 0번째 인덱스에 중요도가 가장 높은 값이 오도록 반복
# arr[0]의 값이 가장 중요도가 높은 값이라면, 해당 문서가 가장 처음 몇 번째 문서였는지를 기억하기 위해 answer에 담아준다.
# arr에서 해당 문서를 출력하고 location에 위치한 값이 몇 번째로 출력되는 지 구하기 위해 arr에 값이 있는 동안 반복한다.

from collections import deque
def solution(arr, location):
    arr = deque(arr)
    index = deque([i for i in range(len(arr))])
    answer = []

    while arr:
        if arr[0] == max(arr):
            answer.append(index.popleft())
            arr.popleft()    
        else:
            arr.append(arr.popleft())
            index.append(index.popleft())
            
    return answer.index(location)+1
