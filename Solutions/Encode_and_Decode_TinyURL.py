import string
import random
class Codec:

    alpha = string.ascii_letters + '0123456789'
    def __init__(self):
        self.url2short = {}
        self.short2url = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.url2short:
            code = ''.join(random.choice(self.alpha) for _ in range(6))
            if code not in self.short2url:
                self.url2short[longUrl] = code
                self.short2url[code] = longUrl
                return 'http://tinyurl.com/' + code
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
print(codec.decode(codec.encode(url)))