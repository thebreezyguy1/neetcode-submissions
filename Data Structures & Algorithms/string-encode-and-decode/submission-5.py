class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        encoded_str = ""
        lengths = []
        for word in strs:
            lengths.append(str(len(word)))
        
        print(",".join(lengths) + "#" + "".join(strs))
        
        return ",".join(lengths) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        strs = []
        lengths = []
        encoded_str = ""
        i = 0
        
        while True:
            length = ""
            while s[i].isnumeric():
                length += s[i]
                i += 1
            print(length)
            lengths.append(int(length))
            if s[i] == "#":
                break

            i += 1

        encoded_str = s[i+1:]
        
        for length in lengths:
            word = encoded_str[:length]
            encoded_str = encoded_str[length:]
            strs.append(word)
        
        return strs
