class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endWord = True

    def search(self, word: str) -> bool:
        
        def dfs(node, idx):
            if idx == len(word):
                return node.endWord

            if word[idx] == ".":
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
            
            if word[idx] in node.children:
                return dfs(node.children[word[idx]], idx+1)
            
            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)