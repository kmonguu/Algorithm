# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환

# 예시
# arr1 = [[1, 2]]   arr2 = [[3, 4]]   반환값 = [[4, 6]]


# 내가 푼 코드
# for문으로 2차원 배열을 돌면서 zip으로 두 배열을 묶고 합을 answer에 2차원 배열로 담는다.

def solution(arr1, arr2): 
    answer = []
    
    for i in range(len(arr1)):
        answer.append(list(x + y for x, y in zip(arr1[i], arr2[i])))
    
    return answer




# zip 함수를 2번 사용하여 조금 더 단순하게 푸는 방법

def solution(arr1, arr2):
    return [[a + b for a, b in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]




# 2중 for문으로 푸는 방법

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1
