function solution(sizes) {
  let arr = sizes.map(([w, h]) => (w > h ? [w, h] : [h, w]));

  let result = [0, 0];
  arr.forEach(([w, h]) => {
    if (w > result[0]) result[0] = w;
    if (h > result[1]) result[1] = h;
  });
  return result[0] * result[1];
}
