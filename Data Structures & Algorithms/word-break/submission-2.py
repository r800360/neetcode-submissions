class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ALPHABET = 26
        ROOT = 0
        NONE = -1

        # Each node stores transitions for all 26 lowercase letters.
        nxt = [[NONE] * ALPHABET]
        fail = [ROOT]
        out = [NONE]       # Nearest terminal failure ancestor
        word_len = [0]     # Nonzero iff this node ends a word

        # 1. Build the Trie.
        for word in wordDict:
            node = ROOT

            for ch in word:
                c = ord(ch) - ord('a')
                child = nxt[node][c]

                if child == NONE:
                    child = len(nxt)
                    nxt[node][c] = child
                    nxt.append([NONE] * ALPHABET)
                    fail.append(ROOT)
                    out.append(NONE)
                    word_len.append(0)

                node = child

            word_len[node] = len(word)

        # 2. Build failure links and complete transitions.
        queue = deque()

        # Root's missing transitions loop back to the root.
        for c in range(ALPHABET):
            child = nxt[ROOT][c]

            if child == NONE:
                nxt[ROOT][c] = ROOT
            else:
                fail[child] = ROOT
                out[child] = NONE
                queue.append(child)

        while queue:
            v = queue.popleft()

            for c in range(ALPHABET):
                u = nxt[v][c]

                if u == NONE:
                    # Follow the failure transition in O(1).
                    nxt[v][c] = nxt[fail[v]][c]
                else:
                    f = nxt[fail[v]][c]
                    fail[u] = f

                    # Nearest terminal node on the failure chain.
                    if word_len[f] > 0:
                        out[u] = f
                    else:
                        out[u] = out[f]

                    queue.append(u)

        # 3. Scan s and update DP online.
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        state = ROOT

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            state = nxt[state][c]
            end = i + 1

            # Include the current state if it ends a word;
            # otherwise begin with its nearest terminal suffix.
            v = state if word_len[state] > 0 else out[state]

            while v != NONE:
                length = word_len[v]

                if dp[end - length]:
                    dp[end] = True

                v = out[v]

        return dp[n]