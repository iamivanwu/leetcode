/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  let res = '';
  let word = '';
  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] === ' ') {
      if (word !== ' ') {
        res += word + ' ';
      }
      word = ' ';
    } else {
      if (word === ' ') {
        word = '';
      }
      word = s[i] + word;
    }
  }
  return (res + word).trim();
};
