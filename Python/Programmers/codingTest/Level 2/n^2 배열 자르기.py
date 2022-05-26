# 정수 n, left, right가 주어지고, 아래의 과정을 통해 만들어진 1차원 배열을 [left : right] 범위만큼 출력

# n행 n열 크기의 비어있는 2차원 배열이 있을 때, i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복

# 1. 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 2. 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 3. 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.

# 시간 초과 코드

def solution(n, left, right):
    arr = [[0]*n for i in range(n)]
      
    for idx in range(1, n+1):
        for j in range(1, idx+1):
            
            arr[idx-1][j-1] = arr[j-1][idx-1] = idx
              
    return sum(arr, [])[left: right+1]


# 내가 푼 정답 코드
# 구하고자하는 배열은 범위를 [left:right+1]로 하기 때문에 2차원 배열을 모두 구하지 않고 풀 수 있다.

# n이 3일 때,
# [1][1] = 1  [1][2] = 2  [1][3] = 3
# [2][1] = 2  [2][2] = 2  [2][3] = 3
# [3][1] = 3  [3][2] = 3  [3][3] = 3

# 위와 같은 2차원 배열이 나오는 것을 볼 수 있는데, 여기서 행과 열 중 큰 수가 그 배열의 값이 되는 것을 확인할 수 있다.

def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):
        a = (idx // n) + 1
        b = (idx % n) + 1 
        
        answer.append(max(a, b))

    return answer
