class Node:
    def __init__(self):
        self.children = {}
        self.word_end = False

class Solution:

    class PrefixTree:

        def __init__(self):
            self.trie = Node()

        def insert(self, word: str) -> None:
            trie_ptr = self.trie
            for character in word:
                if character not in trie_ptr.children:
                    trie_ptr.children[character] = Node()

                trie_ptr = trie_ptr.children[character]
            trie_ptr.word_end = True
        
        def __str__(self) -> str:
            lines = ["ROOT"]

            def dfs(node, prefix):
                children = sorted(node.children.items())

                for i, (character, child) in enumerate(children):
                    is_last = i == len(children) - 1
                    connector = "└── " if is_last else "├── "

                    marker = " *" if child.is_word else ""
                    lines.append(
                        prefix + connector + character + marker
                    )

                    extension = "    " if is_last else "│   "
                    dfs(child, prefix + extension)

            dfs(self.trie, "")
            return "\n".join(lines)
            
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # O(m * n * 4 * (3^(t-1)) + s) time and O(s) space
        words_trie = self.PrefixTree()
        for word in words:
            words_trie.insert(word)
        
        m = len(board)
        n = len(board[0])
        word_set = set()

        def backtrack(i, j, trie_ptr, word):
            # print(i, j, word)
            # board[i][j] in trie_ptr->children (words_trie.trie.children)
            if trie_ptr.word_end:
                word_set.add(word)
            
            if i < 0 or i >= m:
                return

            if j < 0 or j >= n:
                return

            character = board[i][j]

            if character == ".":
                return

            if not trie_ptr.children:
                return

            if character not in trie_ptr.children:
                return

            board[i][j] = "."
            word += character
            trie_ptr = trie_ptr.children[character]
            backtrack(i-1, j, trie_ptr, word)
            backtrack(i+1, j, trie_ptr, word)
            backtrack(i, j-1, trie_ptr, word)
            backtrack(i, j+1, trie_ptr, word)
            board[i][j] = character
            
        
        for i in range(m):
            for j in range(n):
                # Algorithm has to be for each square, 4 choices and then 3 choices
                if board[i][j] in words_trie.trie.children:
                    trie_ptr = words_trie.trie
                    word = ""
                    backtrack(i, j, trie_ptr, word)


        return list(word_set)