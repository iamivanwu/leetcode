/**
 * @param {number[][]} fruits
 * @param {number} startPos
 * @param {number} k
 * @return {number}
 */
var maxTotalFruits = function (fruits, startPos, k) {
  const minPos = startPos - k;
  const maxPos = startPos + k;
  let left = 0,
    lf = [];
  let right = 0,
    rf = [];
  for (let i = 0; i <= fruits.length - 1; i++) {
    if (fruits[i][0] >= minPos && fruits[i][0] <= startPos) {
      left += fruits[i][1];
      lf.push([startPos - fruits[i][0], fruits[i][1]]);
    }
    if (fruits[i][0] >= startPos && fruits[i][0] <= maxPos) {
      right += fruits[i][1];
      rf.push([fruits[i][0] - startPos, fruits[i][1]]);
    }
    if (fruits[i][0] > maxPos) {
      break;
    }
  }

  let i = 0;
  let j = 0;
  let res = Math.max(left, right);

  while (i <= lf.length - 1 && j <= rf.length - 1) {
    if (rf[j][0] === 0) {
      j += 1;
      continue;
    } else {
      while (j <= rf.length - 1) {
        if (rf[j][0] * 2 + lf[i][0] <= k) {
          left = left + rf[j][1];
          res = Math.max(res, left);
          j += 1;
        } else {
          break;
        }
      }
    }
    left = left - lf[i][1];
    i += 1;
  }
  i = lf.length - 1;
  j = rf.length - 1;
  while (j >= 0 && i >= 0) {
    if (lf[i][0] === 0) {
      i -= 1;
      continue;
    } else {
      while (i >= 0) {
        if (lf[i][0] * 2 + rf[j][0] <= k) {
          right = right + lf[i][1];
          res = Math.max(res, right);
          i -= 1;
        } else {
          break;
        }
      }
    }
    right = right - rf[j][1];
    j -= 1;
  }
  return res;
};
