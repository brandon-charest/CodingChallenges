"""
535. Encode and Decode TinyURL
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short
URL such as http://tinyurl.com/4e9iAk.
"""


class Codec:
    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        self.urls.append(longUrl)
        tiny_url_template = "http://tinyurl.com/"
        return tiny_url_template + str(len(self.urls) - 1)

    def decode(self, shortUrl):
        return self.urls[int(shortUrl.split('/')[-1])]


url = "https://leetcode.com/problems/design-tinyurl"
encoder = Codec()

tiny_url = encoder.encode(url)
original_url = encoder.decode(tiny_url)
print(tiny_url)
print(original_url)
