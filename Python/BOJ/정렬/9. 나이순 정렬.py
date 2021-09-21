# N개의 나이와 이름을 공백으로 구분되도록 입력받고 나이순으로 정렬할 때 나이가 같다면 먼저 가입한 사람이 먼저 출력
# lambda식으로 정렬기준을 정함


import sys
input = sys.stdin.readline

word = [input().split() for _ in range(int(input()))]
word.sort(key=lambda x: int(x[0]))                      # lambda 식으로 첫 번째 요소인 나이를 먼저 정렬하도록 함

for i in word:
  print(i[0], i[1])                                     # 나이를 먼저 출력하고 나이가 같으면 입력받은 순으로 출력된다.
  
  

  
  
# 다른 풀이
import sys
input = sys.stdin.readline

word = [input() for _ in range(int(input()))]
word.sort(key=lambda x: int(x.split()[0]))             # 첫 번째 요소인 나이를 공백으로 구분하여 오름차순 정렬 
print("".join(word))                                   # for문을 사용하지 않고 word 리스트의 요소를 출력
