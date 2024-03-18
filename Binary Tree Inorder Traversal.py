from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode)->List[int]:
    result = []
    def dfs(node):
        if not node: return None
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(inorderTraversal(root))