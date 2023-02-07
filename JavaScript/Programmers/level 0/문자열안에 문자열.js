// str1 안에 str2가 있다면 1을 없다면 2를 반환

// 예제
// str1                         str2   result
// "ab6CDE443fgh22iJKlmn1o"     "6CD"    1
// "ppprrrogrammers"            "pppp"   2


// 내가 푼 코드
// 자바스크립트의 내장함수 includes를 이용해, str1 문자열 안에 str2가 있다면 1반환, 없다면 2반환

function solution(str1, str2) {
    return str1.includes(str2) ? 1 : 2
}
