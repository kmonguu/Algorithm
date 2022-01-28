// 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 반환하는 문제

// 내가 푼 문제
// toString 메소드를 이용하여 n을 문자열로 변환하고, 스프레드 문법을 이용하여 변환된 문자열 배열로 변환한다.
// reverse를 사용하여 문자열의 정렬은 바꾸지 않으면서 뒤집어 준다.
// map으로 숫자 배열로 변환하여 반환한다.

function solution(n) {
    return [...n.toString()].reverse().map(x => parseInt(x));
}
