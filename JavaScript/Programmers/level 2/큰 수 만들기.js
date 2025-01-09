function solution(number, k) {
  const numberArr = Array.from(String(number), Number);
  let answer = [];

  for (let i in numberArr) {
    while (
      k > 0 &&
      answer.length > 0 &&
      numberArr[i] > answer[answer.length - 1]
    ) {
      answer.pop();
      k -= 1;
    }
    answer.push(numberArr[i]);
  }
  return answer.slice(0, answer.length - k).join("");
}
