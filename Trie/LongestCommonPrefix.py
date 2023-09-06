#https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.number = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr.number +=1
            curr = curr.children[c]
        curr.endOfWord = True
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for word in strs:
            self.insert(word)
        cur = self.root
        res = ""
        while cur and cur.number ==1 and not cur.endOfWord:
            for letter in cur.children:
                res += letter
                cur = cur.children[letter]
                break
        return res
        



        
