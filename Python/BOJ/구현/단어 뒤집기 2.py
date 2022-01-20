# 문자열 s가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 할 때 다음과 같은 규칙을 지킨다.
# 1. 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
# 2. 문자열의 시작과 끝은 공백이 아니다.
# 3. '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.


# 예시
# baekjoon online judge 이 입력으로 주어지면 noojkeab enilno egduj이 출력된다.
# <open>tag<close> 이 입력으로 주어지면 <open>tag<close> '<'와 '>' 안의 문자는 그대로, 그 외의 문자는 뒤집힌 형태로 출력된다.


# 풀이
# 뒤집을지의 여부를 확인하는 flag를 False로 두어 for문 안에서 조건을 크게 False일 때와 True일 때로 나눈다.

import sys
input = sys.stdin.readline

s = list(input().strip())

flag = False
word = ''
answer = ''

for i in s:
  if not flag:            # flag가 False일 때
    if i == '<':          # '<'을 민나는 순간 flag를 True로 전환하고 flag가 True인 경우로 넘어간다.
      word += i
      flag = True

    elif i == ' ':        # 공백을 만난다면 뒤집는 대상이 공백으로 구분되므로 한 단어가 끝났다는 의미가 된다.
      word += i           # 이 공백을 word에 저장하고
      answer += word      # word에 저장된 공백을 answer에 저장한다.
      word = ''           # 다음 알파벳으로 넘어가기 위해 word는 초기화해준다.

    else:                 # '<'와 공백이 아닌 그 외의 경우
      word = i + word     # 단어를 뒤집어 word에 저장한다.

  elif flag:              # flag가 True인 경우
    word += i             # 알파벳 i를 뒤집지 않고 그대로 word에 저장한다.
    if i == '>':          # 그러다 '>'을 만나면 
      flag = False        # flag를 다시 False로 전환하고 flag가 False일 때로 넘어간다.
      answer += word      # 현재까지 word에 저장된 단어를 answer에 담아주고 word는 초기화해준다.
      word = ''
print(answer + word)
