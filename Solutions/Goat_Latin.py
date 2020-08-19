class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = []
        words = S.split(' ')
        vowel = ['a','e','i','o','u']
        count = 1
        for word in words:
            if word[0].lower() in vowel:
                modified = word + 'ma'
            else:
                modified = word[1:] + word[0] + 'ma'
            for _ in range(count):
                modified += 'a'
            count += 1
            ans.append(modified)
        return (' ').join(ans)
S = "I speak Goat Latin"
print(Solution().toGoatLatin(S))