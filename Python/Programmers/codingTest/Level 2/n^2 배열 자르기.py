# 정수 n, left, right가 주어집니다. 아래의 과정을 통해 만들어진 1차원 배열을 [left : right] 범위만큼 출력

# 1. n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# 2. i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 3. 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 4. 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 5. 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.

# 시간 초과 코드

def solution(n, left, right):
    arr = [[0]*n for i in range(n)]
      
    for idx in range(1, n+1):
        for j in range(1, idx+1):
            
            arr[idx-1][j-1] = arr[j-1][idx-1] = idx
              
    return sum(arr, [])[left: right+1]
