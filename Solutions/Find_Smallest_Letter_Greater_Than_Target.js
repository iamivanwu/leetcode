/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function (letters, target) {
  let l = 0;
  let r = letters.length - 1;
  let res = 0;
  while (l <= r) {
    let mid = Math.floor((l + r) / 2);
    if (letters[mid] <= target) {
      l = mid + 1;
    } else {
      res = mid;
      r = mid - 1;
    }
  }
  return letters[res];
};
