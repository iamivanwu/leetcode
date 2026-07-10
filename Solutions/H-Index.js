/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function (citations) {
  citations.sort((a, b) => a - b);
  let ans = 0;
  let i = 0;
  while (i < citations.length) {
    while (ans < citations[i] && ans < citations.length - i) {
      ans++;
    }
    i++;
  }
  return ans;
};
