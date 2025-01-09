function solution(number, k) {
  let answer = [];

  for (let i in number) {
    while (
      k > 0 &&
      answer.length > 0 &&
      number[i] > answer[answer.length - 1]
    ) {
      answer.pop();
      k -= 1;
    }
    answer.push(number[i]);
  }
  return answer.slice(0, answer.length - k).join("");
}
