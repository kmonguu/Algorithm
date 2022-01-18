// 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환

// 예시
// arr1 = [[1, 2]]   arr2 = [[3, 4]]   반환값 = [[4, 6]]

// 내가 푼 코드

function solution(arr1, arr2) {
    var answer = [];
    
    for (let i = 0; i < arr1.length; i++){
        let arr = []
        for (let j = 0; j < arr1[i].length; j++){
            arr.push(arr1[i][j] + arr2[i][j]);
        }
        answer.push(arr)
    }
    return answer;
}
