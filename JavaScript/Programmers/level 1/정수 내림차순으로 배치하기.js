// 정수 n을 매개변수로 받아, n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운 정수를 반환

// 내가 푼 코드
// 매개변수로 받은 정수 n을 문자열 배열로 만들어 내림차순으로 정렬한다.
// map함수를 사용하여 문자열 배열을 정수 배열로 형변환 한 것을 answer 변수에 담는다.

function solution(n)  {
    let answer = n.toString().split('').sort().reverse().map(x => parseInt(x))
    return Number(answer.join(''));
}
