from collections import deque

class TextEditor:
    """
    Have two arrays left and right where the cursor is at the right of the left array
    """
    def __init__(self):
        self.left = []
        self.right = deque([])

        

    def addText(self, text: str) -> None:
        for ch in text:
            self.left.append(ch)

    def deleteText(self, k: int) -> int:
        numDeleted = 0
        while k > 0 and self.left:
            self.left.pop()
            k -= 1
            numDeleted += 1

        return numDeleted

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.left:
            ch = self.left.pop()
            self.right.appendleft(ch)
            k -= 1

        lenLeft = min(10, len(self.left))
        return ''.join(self.left[len(self.left) - lenLeft:])


    def cursorRight(self, k: int) -> str:
        while k > 0 and self.right:
            ch = self.right.popleft()
            self.left.append(ch)
            k -= 1

        lenLeft = min(10, len(self.left))
        return ''.join(self.left[len(self.left) - lenLeft:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)