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

        stack = [(self.trie, 0)]
        
        while stack:
            node, i = stack.pop()

            if i == len(word):
                if node.word_end:
                    return True
                continue

            char = word[i]
            
            if char == ".":
                for child in node.children.values():
                    stack.append((child, i+1))
            else:
                child = node.children.get(char)
                if child:
                    stack.append((child, i+1))
        
        return False