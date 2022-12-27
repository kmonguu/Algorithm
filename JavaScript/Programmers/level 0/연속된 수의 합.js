// 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 
// 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 반환

// 예제
// num | total
// 3   |  12	-> [3, 4, 5]
// 5   |  15	-> [1, 2, 3, 4, 5]
// 4   |  14	-> [2, 3, 4, 5]


// 내가 푼 코드

// total에서 num을 나눈 몫의 올림값은 평균값으로 구해질 연속된 수의 중앙값이 된다.
// 연속된 수가 시작되는 시작값을 구하려면 중앙값에서 중앙값의 자릿수만큼 빼주면 된다.
// 중앙값의 자릿수는 연속된 수의 개수인 num에 2를 나누어 버림한 값이다.

// 위 과정으로 구해진 시작값으로 num개수만큼 배열을 채우면 된다.

function solution(num, total) {
    
    const startNum = Math.ceil(total / num - Math.floor(num / 2));
    return(Array(num).fill().map((_,i)=>{return i+startNum}))
    
}
