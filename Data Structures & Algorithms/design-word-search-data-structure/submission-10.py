class Node:
    def __init__(self):
        self.children = {}
        self.word_end = False

class WordDictionary:

    def __init__(self):
        self.trie = Node()
        self.word_set = set()
        self.word_len_set = set()

    def addWord(self, word: str) -> None:
        self.word_set.add(word)
        self.word_len_set.add(len(word))
        trie_ptr = self.trie
        for character in word:
            if character not in trie_ptr.children:
                trie_ptr.children[character] = Node()
            
            trie_ptr = trie_ptr.children[character]
        trie_ptr.word_end = True

    def search(self, word: str) -> bool:
        if len(word) not in self.word_len_set:
            return False
        
        if word in self.word_set:
            return True
        
        if not self.trie.children:
            return False

        stack = [self.trie]
        current_idx = 0
        while stack:
            node = stack.pop()

            if node.word_end and current_idx == len(word):
                return True

            if current_idx >= len(word):
                return False
            
            if word[current_idx] == ".":
                if not node.children:
                    return False
                for key in node.children:
                    stack.append(node.children[key])
            elif word[current_idx] in node.children:
                stack.append(node.children[word[current_idx]])
            else:
                continue
            
            current_idx += 1
        
        return False