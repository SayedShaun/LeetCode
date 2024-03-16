class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1:
        return root2
    if not root2:
        return root1
    merged = TreeNode(root1.val+root2.val)
    merged.left = mergeTrees(root1.left, root2.left)
    merged.right = mergeTrees(root1.right, root2.right)
    return merged

def travarsalTree(root: TreeNode) -> None:
    if not root: return None
    print(root.val)
    travarsalTree(root.left)
    travarsalTree(root.right)

#root1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
#root2
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

output = mergeTrees(root1, root2)
travarsalTree(output)


        