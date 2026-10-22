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

        # run BFS from beginWord, removing words from the set as we go
        queue = deque()
        queue.append(beginWord)
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                currentWord = queue.popleft()
                if currentWord == endWord:
                    return level
                wordSet.discard(currentWord)
                for word in wordSet:
                    if self.differByOne(currentWord, word, n):
                        queue.append(word)

        return 0