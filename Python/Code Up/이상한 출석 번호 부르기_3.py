#빈리스트에 값을 입력하고 입력값 중에서 가장 작은 값인 최솟값을 찾는 문제였음
#내장함수 min()을 사용하거나 sort 정렬을 한 후, 제일 첫번째 값을 출력하는 방법과 if문을 사용하여 최솟값을 찾아낼 수 있다.

num = int(input())
k = list(map(int, input().split()))
a = k[0]              #a를 k[0]으로 초기화한다.
for i in range(num): 
  if(a>k[i]):         #최소값 변수 a보다 입력값이 담긴 k[i]가 작다면
    a=k[i]            #최소값 변수 a에 이 입력값을 집어넣음
print(a)
