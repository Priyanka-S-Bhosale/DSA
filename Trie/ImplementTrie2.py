#https://www.codingninjas.com/studio/problems/implement-trie_1387095?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = 0
        self.countPrefix = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
            curr.countPrefix +=1
        curr.endOfWord +=1
        

    def countWordsEqualTo(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return 0
            curr = curr.children[letter]
        if curr.endOfWord != 0: return curr.endOfWord
        else: return 0
        

    def countWordsStartingWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return 0
            curr = curr.children[letter]
        return curr.countPrefix
    
    def erase(self, word):
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return
            curr = curr.children[letter]
            curr.countPrefix -=1
        curr.endOfWord -=1
