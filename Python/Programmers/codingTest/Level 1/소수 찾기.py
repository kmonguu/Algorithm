# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환

# 내가 푼 코드
# answer에 n의 크기만큼 배열을 할당하고 True로 초기화
# 0과 1은 소수가 아니므로 False를 저장한다.
# 만약, i가 소수라면 i의 배수는 소수가 아니므로 i의 배수들은 False로 저장한다.
# answer에서 True인 것만 찾아 개수를 세어 반환한다.

def solution(n):
    answer = [True]*(n+1)
    answer[0] = answer[1] = False
    
    for i in range(2, int(n**0.5)+1):
        for j in range(i*i, n+1, i):
            answer[j] = False
    return answer.count(True)
    
        
