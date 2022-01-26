# 검색 결과가 먼저 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력
# 패턴에는 알파벳과 "." 그리고 "?"만 넣을 수 있다. 가능하면 ?을 적게 써야 한다. 그 디렉토리에는 검색 결과에 나온 파일만 있다고 가정하고, 파일 이름의 길이는 모두 같다.

# 예시
# 파일명의 첫 번째 글자가 a이고 세 번째 글자가 b이고 확장자가 exe인 파일 acb.exe, aab.exe를 결과로 찾기위해서는
# dir a?b.exe 라고 검색해야 한다.


# 내가 푼 코드
# 첫 번째로 입력되는 파일 이름을 기준으로 탐색하기 위해 n-1번 다른 파일 이름을 리스트로 입력받고 탐색을 반복한다.
# 첫 번째 리스트와 다른 n-1개의 파일을 비교하여 인덱스는 같지만 값이 서로 다르다면 '?'로 변환한다.

import sys
input = sys.stdin.readline

n = int(input())
word = list(input().strip())

for _ in range(n-1):
  other = list(input().strip())
  for i in range(len(word)):
    if word[i] != other[i]:
      word[i] = '?'

print(''.join(word))
