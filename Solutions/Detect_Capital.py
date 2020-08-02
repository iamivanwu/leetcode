class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return False
        count = 0
        for c in word:
            if c.isupper():
                count += 1
        if word[0].isupper():
            return True if count == 1 or count == len(word) else False
        else:
            return True if count == 0 else False