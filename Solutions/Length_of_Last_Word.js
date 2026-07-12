/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  let cur = 0;
  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] !== ' ') {
      cur += 1;
    } else if (s[i] === ' ' && cur !== 0) {
      break;
    }
  }
  return cur;
};
