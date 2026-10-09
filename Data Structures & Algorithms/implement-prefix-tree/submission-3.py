class Node:
    def __init__(self):
        self.children = {}


class PrefixTree:

    def __init__(self):
        self.trie = Node()
        self.word_set = set()

    def insert(self, word: str) -> None:
        self.word_set.add(word)
        trie_ptr = self.trie
        for character in word:
            if character not in trie_ptr.children:
                trie_ptr.children[character] = Node()

            trie_ptr = trie_ptr.children[character]

    def search(self, word: str) -> bool:
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.word_set:
            return True
        trie_ptr = self.trie
        for character in prefix:
            if character not in trie_ptr.children:
                return False

            trie_ptr = trie_ptr.children[character]
        
        return True
        