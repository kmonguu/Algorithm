# 양수와 +, -가 포함된 식에서 괄호를 적절히 쳐서 이 식의 값을 최소로 출력


# 풀이
# 식에서 -가 나올 때까지 앞의 식을 모두 더하다가 -를 만난다면 이후 뒤의 식은 모두 빼도록 괄호를 쳐야한다.
# 예를 들어, 55-50+40이라는 식이 있다면 이 식을 55-(50+40)으로 괄호를 쳐주면 -35라는 최솟값을 구할 수 있다.
# -를 기준으로 식을 자르고, '-'를 기준으로 잘려진 앞쪽의 식은 더해주고, '-'를 기준으로 잘려진 뒷쪽의 식은 -50, -40 과 같이 빼주면 된다.


# 코드
arr = input().split('-')

sum = 0
for i in arr[0].split('+'):
  sum += int(i)

for i in arr[1:]:
  for j in i.split('+'):
    sum -= int(j)

print(sum)




# 다른 풀이
expr = input().split("-")

result = sum(map(int, expr[0].split("+")))
for e in expr[1:]:
  result -= sum(map(int, e.split("+")))

print(result)
