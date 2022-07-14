class Codec:
    
    def __init__(self):
        self.mp = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_ = hash(longUrl)
        hash_ = -1*hash_ if hash_<0 else hash_
        tiny = "http://tinyurl.com/"+str(hash_)
        self.mp[tiny] = longUrl
        return tiny

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.mp[shortUrl]
 