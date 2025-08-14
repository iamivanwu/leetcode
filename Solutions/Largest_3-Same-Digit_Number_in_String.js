/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function (num) {
  let max = "";
  let cur = "";
  for (let i = 0; i <= num.length - 1; i++) {
    if (i === 0) {
      cur = num[i];
      continue;
    }
    if (num[i] !== num[i - 1]) {
      cur = num[i];
    } else {
      cur += num[i];
    }
    if (cur.length === 3) {
      if (!max || +cur[0] > +max[0]) {
        max = cur;
      }
    }
  }
  return max;
};
