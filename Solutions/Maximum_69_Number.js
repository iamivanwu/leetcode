/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function (num) {
  const s = num.toString();
  let n = '';
  let f = false;
  for (let i = 0; i <= s.length - 1; i++) {
    if (s[i] === '6' && !f) {
      n += '9';
      f = true;
    } else {
      n += s[i];
    }
  }
  return +n;
};
