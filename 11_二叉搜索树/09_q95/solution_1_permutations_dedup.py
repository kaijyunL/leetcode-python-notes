from itertools import permutations
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Optional[TreeNode]) -> str:
    if not root:
        return "#"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        unique_trees: Dict[str, TreeNode] = {}

        for order in permutations(range(1, n + 1)):
            root = None
            for value in order:
                root = self.insert(root, value)

            # 用先序序列化结果做去重键
            key = serialize(root)
            if key not in unique_trees:
                unique_trees[key] = root

        return list(unique_trees.values())

    def insert(self, root: Optional[TreeNode], value: int) -> TreeNode:
        if not root:
            return TreeNode(value)

        if value < root.val:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root


if __name__ == "__main__":
    solution = Solution()
    test_cases = [0, 1, 3]

    for n in test_cases:
        trees = solution.generateTrees(n)
        print(f"n = {n}, count = {len(trees)}")
        if n <= 3:
            serializations = sorted(serialize(tree) for tree in trees)
            print(serializations)
