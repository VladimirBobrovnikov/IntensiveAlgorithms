from typing import List
from collections import defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    dict_data = defaultdict(list)
    visited = set()
    def build_dict(self, noda: TreeNode):
        if noda.left:
            self.dict_data[noda.val].append(noda.left.val)
            self.dict_data[noda.left.val].append(noda.val)
            self.build_dict(noda.left)
        if noda.right:
            self.dict_data[noda.val].append(noda.right.val)
            self.dict_data[noda.right.val].append(noda.val)
            self.build_dict(noda.right)

    def get_by_distance(self, val: int, k: int):
        if k == 0:
            return [val]
        result = []
        if self.dict_data[val]:
            for elem in self.dict_data[val]:
                if elem not in self.visited:
                    self.visited.add(elem)
                    result.extend(self.get_by_distance(elem, k - 1))
        return result

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.build_dict(root)
        self.visited.add(target.val)
        result = self.get_by_distance(target.val, k)
        self.visited.clear()
        self.dict_data.clear()
        return result
