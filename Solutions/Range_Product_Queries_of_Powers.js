/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var productQueries = function (n, queries) {
  const b = n.toString(2);
  const res = [];
  for (const q of queries) {
    let count = 0;
    let one = -1;
    for (let i = 0; i <= b.length - 1; i++) {
      if (b[b.length - 1 - i] === "1") {
        one += 1;
      }
      if (b[b.length - 1 - i] === "1" && one >= q[0] && one <= q[1]) {
        count += i;
      }
      if (one > q[1]) {
        break;
      }
    }
    res.push(Math.pow(2, count) % 1000000007);
  }
  return res;
};
