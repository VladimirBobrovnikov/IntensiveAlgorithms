from typing import List, Optional
from queue import Queue


class TreeNode:
    def __str__(self):
        return f'TreeNode {self.val=},'

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = []
    queue = Queue()

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result.clear()

        if not root:
            return []

        temp_ = []
        self.queue.put((root, 0))
        lvl_now = 0
        while True:
            if self.queue.empty():
                if temp_:
                    self.result.append(temp_.copy())
                break
            else:
                noda, lvl = self.queue.get()
                if lvl == lvl_now:
                    temp_.append(noda.val)
                else:
                    lvl_now = lvl
                    self.result.append(temp_.copy())
                    temp_.clear()
                    temp_.append(noda.val)
                if noda.left:
                    self.queue.put((noda.left, lvl + 1))
                if noda.right:
                    self.queue.put((noda.right, lvl + 1))

        return self.result
