//정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 반환하되, 반환하려는 배열이 비어있을 경우 배열에 -1을 채워 반환

// 내가 푼 코드
// 스프레드 문법으로 arr배열의 요소를 펼쳐 그 중 최솟값을 구하고, indexOf를 사용하여 최솟값의 인덱스를 찾아 제거한다.
// 만약 arr배열의 길이가 1을 넘지 않는다면 빈 배열이므로 -1을 반환하도록 arr에 [-1]을 저장한다.

function solution(arr) {
    if (1 < arr.length)
        arr.splice(arr.indexOf(Math.min(...arr)),1);
    else
        arr = [-1];
    return arr
   
}
