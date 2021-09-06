# 두 수가 주어졌을 때 예를 들어, 734와 893이 있다면 이 수를 437과 398로 수를 뒤집고 둘 중 큰 수를 출력하는 문제
# reverse를 이용하여 입력받은 숫자를 역순으로 뒤집고 if-else문을 사용하여 둘 중 큰 수를 출력
# reverse를 활용하여 푸는 방법을 통해 reverse와 revered의 차이점을 알게 됨

a, b = map(list,input().split())

a.reverse()           # 입력받은 a변수에 담긴 숫자 역순
b.reverse()           # b변수에 담긴 숫자 역순

if a > b:             # 만약 a > b라면 
  print("".join(a))   # a 출력
else:
  print("".join(b))

  
# 다른 풀이 리스트 슬라이싱을 활용하여 reverse를 사용하지 않고 숫자를 뒤집어 내장함수 max로 큰 수를 출력하였다.
a, b = input().split()
a = a[::-1]			        # 리스트 슬라이싱: 리스트변수명[시작인덱스:종료인덱스:step]
b = b[::-1]		          # reverse() 함수를 사용하지 않고 리스트 내용을 뒤집을 수 있다.
print(max(a, b))
