from typing import Dict, List, Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Optional[TreeNode]) -> str:
    if not root:
        return "#"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"


def clone_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    return TreeNode(root.val, clone_tree(root.left), clone_tree(root.right))


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        memo: Dict[Tuple[int, int], List[Optional[TreeNode]]] = {}

        def build(left: int, right: int) -> List[Optional[TreeNode]]:
            if left > right:
                return [None]

            key = (left, right)
            if key in memo:
                # 取缓存时克隆，避免不同答案共享同一棵子树对象
                return [clone_tree(tree) for tree in memo[key]]

            trees: List[Optional[TreeNode]] = []

            for root_val in range(left, right + 1):
                left_trees = build(left, root_val - 1)
                right_trees = build(root_val + 1, right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)

            # 缓存一份独立副本，后续命中时再克隆返回
            memo[key] = [clone_tree(tree) for tree in trees]
            return trees

        return build(1, n)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [0, 1, 3]

    for n in test_cases:
        trees = solution.generateTrees(n)
        print(f"n = {n}, count = {len(trees)}")
        if n <= 3:
            serializations = sorted(serialize(tree) for tree in trees)
            print(serializations)
