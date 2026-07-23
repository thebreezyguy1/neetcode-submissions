class Solution:

    def __init__(self):
        self.hashmap = {}

    def encode(self, strs: List[str]) -> str:
        string = " ".join(strs)
        self.hashmap[string] = strs
        return string

    def decode(self, s: str) -> List[str]:
        return self.hashmap[s]