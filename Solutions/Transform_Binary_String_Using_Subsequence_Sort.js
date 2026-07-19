/**
 * @param {string} s
 * @param {string[]} strs
 * @return {boolean[]}
 */
var transformStr = function (s, strs) {
    const count = (ss) => {
        let a = 0;
        let b = 0;
        for (const c of ss) {
            if (c === "0") {
                a += 1;
            } else if (c === "1") {
                b += 1;
            }
        }
        return { a, b };
    };
    const { a, b } = count(s);
    const check = (str) => {
        const { a: aa, b: bb } = count(str);
        if (aa > a || bb > b) {
            return false;
        }
        let ci = 0;
        let cj = 0;
        let buffer = s.length - aa - b;
        for (let i = 0; i <= s.length; i++) {
            ci += s[i] === "1" ? 1 : 0;

            if (str[i] === '?') {
                cj += buffer > 0 ? 0 : 1;
                buffer -= 1;
            } else if (str[i] === '1') {
                cj += 1
            }
            if (ci < cj) {
                return false;
            }
        }
        return true;
    };
    const ans = [];
    for (const str of strs) {
        ans.push(check(str));
    }
    return ans;
};