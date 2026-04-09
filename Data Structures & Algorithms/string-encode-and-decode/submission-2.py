class Solution:

    def encode(self, strs: List[str]) -> str:
        terminator = "\0"
        encoded_strs = [my_str + terminator for my_str in strs]
        return "".join(encoded_strs)
    def decode(self, s: str) -> List[str]:
        terminator = "\0"
        return s.split(terminator)[:-1]