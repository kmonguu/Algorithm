# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 반환하되, 반환하려는 배열이 비어있을 경우 배열에 -1을 채워 반환

# 내가 푼 코드
# 매개변수로 들어오는 배열의 길이가 1이면 반환되는 배열이 비어있으므로 경우를 배열의 길이가 1보다 클 때와 아닐 때로 나눈다.
# 배열의 길이가 1보다 클 때, 배열의 순서는 건들이지 않으면서 최솟값만 제거하도록 remove를 사용했다.

# 처음에 입출력 예 1만 보고 배열을 내림차순으로 정렬하여 풀었더니 반환되는 배열의 순서가 달라져서 틀렸음

def solution(arr):
    if len(arr) > 1:
        arr.remove(min(set(arr)))
        return arr
        
    else:
        return [-1]

    
    
# 다른 사람 코드    
# 삼항연산자를 이용하여 조건문만 묶어서 처리

def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]         # 삼항연산자 사용해서 return
