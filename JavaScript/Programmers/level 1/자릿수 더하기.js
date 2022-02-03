// 자연수 N이 주어질 때, N의 각 자릿수의 합을 구해서 반환


// 내가 푼 코드
// 매개 변수 n을 문자열 배열로 만들어서 각 자릿수마다 잘라주고 map 을 이용하여 숫자 배열로 바꿔주었다.
// 정수 배열의 합을 구하기 위해 reduce를 사용

function solution(n)
{
    let answer = [...n.toString()].map(Number);
    return answer.reduce((x, y) => (x + y));
}


// 다른 사람 코드
// map을 사용하지 않고 reduce를 사용하여 배열의 합을 구하는 과정에서 배열 안 요소를 하나씩 정수로 변환하여 누적합을 구한다.

function solution(n)
{
    return [...n.toString()].reduce((x, y) => (x + parseInt(y)), 0);
}



// 문자를 숫자로 바꿀 경우 *1을 해도 변경이 가능
function solution(n) {
    return [...(n + "")].reduce((sum, current) => sum + current * 1, 0);
}
