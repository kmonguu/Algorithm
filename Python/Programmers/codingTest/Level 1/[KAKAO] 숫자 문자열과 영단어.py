#


# 내가 푼 코드
# 0부터 9까지 영단어와 숫자를 담은 딕셔너리를 선언
# answer에 매개변수 s를 복사하고 매개변수로 들어온 문자열에 문자가 있다면 해당 숫자로 교체해주는 replace를 사용함

def solution(s):
    english_word = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    answer = s
    
    for item in english_word.items():
        answer = answer.replace(item[0], str(item[1]))

        
    return int(answer)
