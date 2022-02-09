# 2차원 배열이 매개변수로 주어졌을 때, 이 2차원 배열의 두 대각선에 위치한 값의 합을 구하고
# 두 대각선의 합을 뺀 절댓값을 반환

# 내가 푼 코드
# 왼쪽 모서리에서 시작하는 대각선에 위치한 요소를 더하는 left와
# 오른쪽 모서리에서 시작하는 대각선에 위치한 요소를 더하는 right를 각각 0으로 초기화
# 두 대각선의 요소의 합을 구하고 left와 right에 저장
# left와 right를 뺀 값의 절댓값을 반환

def diagonalDifference(arr):
    # Write your code here
    left, right = 0, 0
    
    for i in range(n):
        left += arr[i][i]
        right += arr[i][(n-1)-i]
    return abs(left - right)
