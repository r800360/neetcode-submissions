# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         terminator = "\0"
#         encoded_strs = [my_str + terminator for my_str in strs]
#         return "".join(encoded_strs)
#     def decode(self, s: str) -> List[str]:
#         terminator = "\0"
#         return s.split(terminator)[:-1]
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)

            i = j + 1 + length

        return decoded