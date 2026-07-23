class Solution:

    def __init__(self):
        self.hashmap = {}

    def encode(self, strs: List[str]) -> str:
        string = " ".join(strs)
        self.hashmap[string] = strs
        return string

    def decode(self, s: str) -> List[str]:
        if s in self.hashmap:
            return self.hashmap[s]
        else:
            return None