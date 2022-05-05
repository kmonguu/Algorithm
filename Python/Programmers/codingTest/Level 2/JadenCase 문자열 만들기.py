# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열이다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 반환

# 내가 푼 코드
# 문자열 s를 공백을 기준으로 잘라 배열을 만들고 단어들로 구성된 새로운 배열을 생성
# 새로 만들어진 배열을 순회하며 각 단어의 첫글자를 capitalize()를 사용하여 JadenCase로 만들고 answer에 저장 후 반환

# <capitalize와 title의 차이>
# capitalize() : 문장의 첫 단어의 첫 글자만 대문자로 바꿈
# title() : 문장의 모든 단어의 첫 글자를 대문자로 바꿈

# 단, title()은 알파벳 이외의 문자(숫자, 특수기호, 띄어쓰기 등)를 기준으로 첫 글자를 대문자로 바꾸기 때문에
# 단어의 첫 글자로 숫자가 들어오면 숫자의 바로 뒤 문자를 첫 글자로 인식하여 대문자로 바꿔줌

def solution(s):
  answer = [word.capitalize() for word in list(map(str, s.split(' ')))]
  return ' '.join(map(str, answer))
