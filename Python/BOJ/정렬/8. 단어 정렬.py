# 알파벳 소문자로 이루어진 N개의 단어를 1. 길이가 짧은 것부터 2. 길이가 같으면 사전 순으로 단어를 정렬한다.
# 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력



import sys
input = sys.stdin.readline

word = (input() for _ in range(int(input())))
word = list(set(word))                                  # 단어를 word라는 변수에 입력받고 set함수를 이용하여 중복 단어를 제거 후 리스트 형태로 저장

word_list = []                                          # 입력받은 단어와 단어를 길이를 저장하기 위해 리스트 생성
for i in word:
  word_list.append((i, len(i)))                         # 리스트에 단어와 단어의 길이를 저장

word_list.sort(key=lambda word: (word[1], word[0]))     # lambda 식을 사용하여 정렬 기준을 세우고 정렬되도록 함

for i in word_list:
  print(i[0].strip())                                   # 리스트에 저장된 첫 번째 인덱스인 단어를 양쪽 strip을 이용하여 공백없이 출력
  
  
  
  
  
# 다른 풀이
import sys
input = sys.stdin.readline

word = list(set([input().rstrip() for _ in range(int(input()))]))
word.sort(key=lambda x: (len(x), x))
print("\n".join(word))
