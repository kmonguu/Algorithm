# 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때,
# A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 반환,
# B가 될 수 없으면 -1을 반환

# 예제
# "hello"	"ohell"	1
# "apple"	"elppa"	-1

# 내가 푼 코드

def solution(A, B):
    cnt = 0
    
    for _ in range(len(A)):
        if A != B:
            A = list(A)
            A = [A[-1]]+A[0:-1]
            cnt +=1
            A = ''.join(A)
            
        else: 
            return cnt
            
    return -1


# 다른 풀이
# 문자열 B를 두 번 합친 값에서 A를 찾아 A문자열이 시작하는 인덱스를 반환, 없으면 -1반환

def solution(A, B):
    B = B+B
    return B.index(A) if A in B else -1
