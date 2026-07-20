class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:
            s += str(len(x)) + "#" + x   # add a delimiter for clarity
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the delimiter to extract the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # extract the string of that length
            word = s[j+1:j+1+length]
            res.append(word)
            # move pointer forward
            i = j + 1 + length
        return res

