class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def char_to_num(char) -> int:
            return ord(char) - ord('a')

        def num_to_char(num):
            return chr(num + ord('a'))
        
        n = len(words)
        graph = defaultdict(set)
        letters = set()
        for char in words[0]:
            letters.add(char_to_num(char))
        for i in range(n - 1):
            first = words[i]
            second = words[i + 1]
            for char in second:
                letters.add(char_to_num(char))
            if first == second:
                continue
            if first.startswith(second):
                # Impossible in a valid lexicographical ordering
                return ""
            if second.startswith(first):
                continue
            # Find the first character where they differ
            for j in range(min(len(first), len(second))):
                if first[j] == second[j]:
                    continue

                key = char_to_num(first[j])
                value = char_to_num(second[j])

                graph[key].add(value)
                break
        
        # print(graph)
        # print(letters)
        # Run Kahn's algorithm to get the valid ordering
        num_letters = len(letters)
        indegree = defaultdict(int)
        for letter in graph:
            for value in graph[letter]:
                indegree[value] += 1
        queue = deque(letter for letter in letters if letter not in indegree or indegree[letter] == 0)
        processed = 0
        result = ""

        while queue:
            letter = queue.popleft()
            result += num_to_char(letter)
            processed += 1

            for value in graph[letter]:
                indegree[value] -= 1

                if indegree[value] == 0:
                    queue.append(value)
        
        if processed != num_letters:
            return ""
        
        return result