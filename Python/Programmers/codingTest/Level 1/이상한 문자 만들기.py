# 문자열 s가 하나 이상의 단어로 구성되어 있을 때, 각 단어는 하나 이상의 공백문자로 구분되어 있다.
# 각 단어의 짝수번째 알파벳은 대문자, 홀수번째 알파벳은 소문자로 바꾼 문자열을 반환

# 내가 푼 코드
# 처음 공백을 기준으로 백준에서 풀었던 문자 뒤집기처럼 공백을 기준으로 잘린 단어를 대소문자를 변경하여 word에 넣고
# 한 단어가 끝났다면 answer배열에 넣어주는 방식으로 풀었고, 각 단어들 사이의 공백을 위해 join을 사용하여 공백을 주었다.
# 하지만 계속 실패가 나와서 질문하기를 보고 split()을 split(" ")로 변경해주었다.
# split()을 사용하면 s문자열의 모든 공백을 없애버리기 때문이다.

def solution(s):
    arr = s.split(" ")
    
    answer = []
    for i in arr:
        word = ''
        for j in range(len(i)):
            if j % 2:     
                word += i[j].lower()
            else:
                word += i[j].upper()
        answer.append(word)

    return ' '.join(answer)



# 다른 사람 풀이
# for문을 사용하여 리스트로 변환된 s의 요소를 순환하여 공백을 만난다면 cnt 초기화, 공백이 아니라면 cnt에 맞춰 대소문자 변환을 해준다.
def solution(s):
    answer = list(s)
    cnt = 0
    for i in range(len(answer)):
        if answer[i] == " ":
            cnt = 0
            continue
        
        answer[i] = answer[i].upper() if cnt % 2 == 0 else answer[i].lower()
        cnt += 1
        
    return "".join(answer)
