class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        END = "#"

        for word in wordDict:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node[END] = True

        n = len(s)
        max_len = max(map(len, wordDict), default=0)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            node = trie
            for j in range(i, min(i + max_len, n)):
                if s[j] not in node:
                    break
                node = node[s[j]]

                if END in node:
                    dp[j + 1] = True

        return dp[n]