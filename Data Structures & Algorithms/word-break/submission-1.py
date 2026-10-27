class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = len(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if dp[-1]:
                return True
            
            if dp[i]:
                for word in wordDict:
                    word_len = len(word)
                    if i + word_len < n + 1 and s[i : i + word_len] == word:
                        dp[i + word_len] = True

        return dp[-1]