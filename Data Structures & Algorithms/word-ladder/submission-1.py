class Solution:
    def differByOne(self, first: str, second: str, n: int) -> bool:
        counter = 0
        for i in range(n):
            if first[i] != second[i]:
                counter += 1
            if counter > 1:
                return False
        
        if counter == 0:
            return False
        
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        patterns = defaultdict(list)

        for word in wordSet | {beginWord}:
            for i in range(n):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        # run BFS from beginWord, removing words from the set as we go
        queue = deque()
        queue.append(beginWord)
        visited = {beginWord}
        level = 1

        while queue:
            for _ in range(len(queue)):
                currentWord = queue.popleft()

                if currentWord == endWord:
                    return level
                
                for i in range(n):
                    pattern = currentWord[:i] + "*" + currentWord[i + 1:]

                    for word in patterns[pattern]:
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)

                    # Each pattern bucket only needs to be processed once
                    patterns[pattern] = []

            level += 1

        return 0