# 수학을 포기한 3명의 학생이 각각 [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 와 같은 패턴으로 문제를 찍으려고 할 때
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 배열 answers에 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 반환


# 풀이
# 학생이 문제를 찍는 패턴을 배열로 만들고 정답과 비교하여 맞춘 문제의 수를 저장하는 score 배열을 만들어 저장
# 만약 동점자가 있을 경우 score배열의 최댓값과 score에 담겨있는 값을 하나하나 비교하며 동점자가 있는 지 확인 후 문제를 가장 많이 맞춘 사람을 반환한다.

# 코드
def solution(answers):
    students = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score = [0]*3                                                             # 3명의 학생들이 맞춘 문제의 수를 저장하는 배열 초기화
    for i in range(len(answers)):
        if (answers[i] == students[0][i%5]):                                  # 첫 번째 학생의 문제 찍기 패턴과 정답을 비교하기 위해 i%5 식을 이용
            score[0] += 1                                                     # 정답과 일치하다면 score[0]에 첫 번째 학생의 맞힌 문제 수를 저장
        if (answers[i]) == students[1][i%8]:                                  # 두 번째 학생
            score[1] += 1
        if (answers[i] == students[2][i%10]):                                 # 세 번째 학생
            score[2] += 1
            
    answer = []        
    for i in range(3):
        if (score[i] == max(score)):                                          # 문제를 가장 많이 맞힌 사람이 한 명이 아닐 수 있으므로 score에 저장된 값을 score의 최댓값과 비교
            answer.append(i+1)                                                # 가장 많은 문제를 맞힌 학생이 여러 명이면 모두 출력을 해야 하므로 i+1하여 학생 번호를 answer에 저장
          
    return answer



# answer 배열에 답을 저장하는 다른 방법
# max 함수를 if문에 사용하여 for문에서 계속 호출시키지 않고 먼저 호출하는 방법이 시간으로 효율적이다.

# 1. max 함수를 미리 호출
answer = []
    max_score = max(check)
    for i in range(3):
        if check[i] == max_score:
            answer.append(i + 1)
            
            
            
# 2. 
answer = []
    max_score = max(check)                                              # max 함수 호출하여 최대값을 max_score에 저장
    if check[0] == max_score: answer.append(1)
    if check[1] == max_score: answer.append(2)
    if check[2] == max_score: answer.append(3)
    

    
 

# 다른 풀이 : enumerate 을 사용한 방법
# enummerate는 리스트를 튜플로 만들어준다.

def solution(answers):
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    check = [0] * 3
    for i in range(len(answers)):
        if answers[i] == students[0][i % 5]: check[0] += 1
        if answers[i] == students[1][i % 8]: check[1] += 1
        if answers[i] == students[2][i % 10]: check[2] += 1
    
    answer = []
    max_score = max(check)
    for idx, score in enumerate(check):
        if score == max_score:
            answer.append(idx + 1)
    
    return answer
