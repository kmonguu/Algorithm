# 배열 arr이 주어질 때, 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있다.
# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 할 때, 제거 후 남은 수들을 반환

# 내가 푼 코드
# answer배열에 배열 arr의 0번째 인덱스 요소를 넣어 선언하고
# arr의 요소와 비교하여 중복값이 발생하지 않도록 answer에 없는 값만 append해주어 배열 arr의 원소들의 순서를 유지하면서
# 중복된 요소의 값을 제거하였다.

def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    return answer
