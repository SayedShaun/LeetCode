class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root:TreeNode)->int:
    length = 0
    def dfs(node):
        nonlocal length
        if not node: return 0
        left_len = dfs(node.left)
        right_len = dfs(node.right)
        length = max(length, left_len+right_len)
        return max(left_len, right_len) + 1
    dfs(root)
    return length

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(diameterOfBinaryTree(root))
        
