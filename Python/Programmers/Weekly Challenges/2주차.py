
def solution(scores):
  answer = ''
  num = len(scores)                             # 학생수 
  
  for i in range(num):                          # 평가한 학생(행)
    score_list = []                             # 점수를 저장할 리스트

    for j in range(num):                        # 평가받은 학생(열)
      score_list.append(scores[j][i])

    max_score = max(score_list)                 # 최댓값 
    max_num = score_list.count(max_score)       # 최댓값의 갯수

    min_score = min(score_list)                 # 최솟값
    min_num = score_list.count(min_score)       # 최솟값의 갯수

    sum_score = sum(score_list)                 # 리스트에 담긴 점수들의 합
    num_score = len(score_list)                 # 리스트에 담긴 점수들의 갯수(길이)
  
    my_score = score_list[i]                    # 자기자신을 평가한 점수

    if max_score == my_score and max_num == 1:  # 자기자신을 평가한 점수가 유일한 최고점일 경우 if문
      sum_score -= my_score                     # 점수들의 합에서 자기자신을 평가한 점수를 빼준다.
      num_score -= 1                            # 자기자신을 평가한 점수가 빠지므로 점수들의 갯수에서도 -1을 해준다.
    
    elif min_score == my_score and min_num == 1: # 자기자신을 평가한 점수가 유일한 최저점일 경우
      sum_score -= my_score                      # 마찬가지로 총합에서 자기자신을 평가한 점수를 뺌
      num_score -= 1                             # 점수의 갯수에서도 -1을 한다.

    result = sum_score/num_score                 # result 변수에 점수들의 총합에 점수의 갯수를 나누어 평균을 구해 저장


    if 90 <= result:                             # 평균 점수가 90점 이상일 때
      answer += 'A'                              # answer 변수에 A를 더해줌

    elif 80 <= result < 90:                      # 평균 점수가 80점 이상 90점 미만
      answer += 'B'                              # answer 변수에 B를 더해줌

    elif 70 <= result < 80:                      # 평균 점수가 70점 이상 80점 미만
      answer += 'C'                              # answer 변수에 C를 더해줌

    elif 50 <= result < 70:                      # 평균 점수가 60점 이상 70점 미만
      answer += 'D'                              # answer 변수에 D를 더해줌
  
    else:                               
      answer += 'F'                              # 그 외의 평균 점수일 경우 F를 더해줌

  return answer                                  # answer에 저장된 값을 return
