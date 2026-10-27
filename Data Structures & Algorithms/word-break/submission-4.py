class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Trie node:
        #   ordinary keys = character transitions
        #   "#" = this node ends a word
        trie = {}
        for word in wordDict:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = True

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            node = trie
            for j in range(i, n):
                ch = s[j]
                if ch not in node:
                    break

                node = node[ch]
                if "#" in node:
                    dp[j + 1] = True

                    # Safe early exit: this prefix is segmentable
                    # and reaches the end of s.
                    if j + 1 == n:
                        return True

        return dp[n]