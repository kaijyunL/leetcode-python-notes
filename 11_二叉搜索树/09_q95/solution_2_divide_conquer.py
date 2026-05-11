from typing import List, Optional


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

        def build(left: int, right: int) -> List[Optional[TreeNode]]:
            if left > right:
                # 空树也要算一种合法选择，方便后面做组合
                return [None]

            trees: List[Optional[TreeNode]] = []

            for root_val in range(left, right + 1):
                left_trees = build(left, root_val - 1)
                right_trees = build(root_val + 1, right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        # 把左边每一种和右边每一种逐个配对
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)

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
