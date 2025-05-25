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
            if ch in cur.children:
                cur = cur.children[ch]
            cur.children[ch] = TrieNode()

        cur.endWord = True

    def searchWord(self, word: str) -> bool:
        """
        Need DFS so that you can explore all paths in children in the case of a .
        """

        def dfs(node: TrieNode, idx: int) -> bool:
            if idx == len(word):
                return node.endWord
            
            if word[idx] == ".":
                #explore all paths in children 
                for ch in node.children:
                    if dfs(node.children[ch], idx + 1):
                        return True

            if word[idx] in node.children: 
                return dfs(node.children[word[idx]], idx + 1)
            
            return False
        
        return dfs(self.root, 0)

    