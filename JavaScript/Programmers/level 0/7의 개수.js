// 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 반환

// 예제
[7, 77, 17]  4
[10, 29]     0

// 내가 푼 코드
function solution(array) {
    return array.join('').split('7').length-1;
}
