# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값 반환
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다.
# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 빌려줄 수 있다.


# 풀이
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 경우가 있다면 이 학생은 lost 배열에도 존재하고 reserve 배열에도 존재할 수 있다.
# 이 학생은 체육복을 하나만 도난당했다고 가정하고 남은 체육복이 하나이기 때문에 다른 학생에게 빌려줄 수 없게 된다.
# 이러한 경우를 제외하기 위해 lost와 reserve를 set를 이용하여 두 배열의 중복을 제거해준다.
# reserve에 있는 학생들이 바로 앞번호나 바로 뒷번호 학생에게만 체육복을 빌려줄 수 있으므로 경우의 수를 나누어 lost에 있는 지 확인하면 된다.


# 틀린 풀이
# lost와 reserve에 중복되는 학생을 고려하지 못함

def solution(n, lost, reserve):
    answer = n - len(lost)
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
            answer += 1
            
        elif i+1 in lost:
            lost.remove(i+1)
            answer += 1
    return answer

  
  
# 정답 풀이

def solution(n, lost, reserve):
    set_reserve = sorted(list(set(reserve) - set(lost)))        
    set_lost = sorted(list(set(lost) - set(reserve)))
    
    answer = n - len(set_lost)
    for i in set_reserve:
        if i-1 in set_lost:
            answer += 1
            set_lost.remove(i-1)
            
        elif i+1 in set_lost:
            answer += 1
            set_lost.remove(i+1)
            
    return answer
  
  
  
  
# 코드 정리

def solution(n, lost, reserve):
    set_reserve = sorted(set(reserve) - set(lost))  # lost와 reserve 배열의 순서가 오름차순으로 되어있지 않은 경우를 고려하여 set 한 후, sorted로 정렬해준다.
    set_lost = sorted(set(lost) - set(reserve))
    
    for i in set_reserve:
        if i-1 in set_lost:                         # set_reserve의 i에서 -1한 값이 set_lost에 있는 경우
            set_lost.remove(i-1)                    # 그 값을 set_lost에서 remove를 이용하여 제거한다.
                                                    # 체육복을 빌린 학생은 set_lost에서 제거해주어야 중복으로 빌려지지 않는다.
        elif i+1 in set_lost:                   
            set_lost.remove(i+1)
            
    return n - len(set_lost)
