from typing import List
import collections
class TreeNode:
    def __init__(self):
        self.end = False
        self.children = collections.defaultdict(TreeNode)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if not cur.children.get(c):
                return False
            else:
                cur = cur.children[c]
        return True if cur.end else False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if not cur.children.get(c):
                return False
            else:
                cur = cur.children[c]
        return True
