from collections import defaultdict
import string, random

class Codec:
    codeDB, urlDB = defaultdict(), defaultdict()
    chars = string.ascii_letters + string.digits

    def getCode(self) -> str:
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code

    def encode(self, longUrl: str) -> str:
        if longUrl in self.urlDB:
            return self.urlDB[longUrl]
        code = self.getCode()
        while code in self.codeDB:
            code = getCode()
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code

    def decode(self, shortUrl: str) -> str:
        return self.codeDB[shortUrl]

def main():
    obj = Codec()
    url = input("Enter the URL to encode: ")
    print(obj.encode(url))
    return obj.decode(obj.encode(url))
    
if __name__ == "__main__":
    print(main())

