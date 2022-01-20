# 주어진 수 num이 1이 될 때까지 다음 작업을 반복했을 때, 작업을 몇 번 반복해야하는지 반환(작업을 500번을 반복해도 1이 되지 않는다면 -1반환)
# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.


# 내가 푼 코드
# 테스트 13번만 자꾸 틀려서 질문하기를 보고 num이 1인 경우 0을 반환하도록 수정
# cnt가 500이 넘어가는 경우 -1을 반환해야 하므로 cnt가 500일 때 break를 해줌

def solution(num):
    cnt = 0
    
    while True:
        if num == 1:
            break
        if cnt == 500:
            break
        if num %2 == 0:
            num //= 2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1
            
    return cnt if cnt != 500 else -1
