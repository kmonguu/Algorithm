// 정수 n을 매개변수로 받아, n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운 정수를 반환

// 내가 푼 코드
// 매개변수로 받은 정수 n을 문자열 배열로 만들어 내림차순으로 정렬한다.
// map함수를 사용하여 문자열 배열을 정수 배열로 형변환 한 것을 answer 변수에 담는다.

function solution(n)  {
    let answer = n.toString().split('').sort().reverse().map(x => parseInt(x))
    return Number(answer.join(''));
}



// 다른 사람 코드
// toString 메소드를 이용하여 n을 문자열로 변환하고, 스프레드 문법을 이용하여 변환된 문자열을 배열로 변환한다.
// 화살표 함수를 사용하여 문자열 배열을 내림차순으로 정렬한다.
// join메소드를 사용하여 정렬된 배열을 하나의 문자열로 join해준다.
// +로 정수로 변환하여 반환한다.

function solution(n) {
    return +[...n.toString()].sort((a, b) => b - a).join("");
}
