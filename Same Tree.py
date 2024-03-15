class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sameTree(p: TreeNode, q: TreeNode)->bool:
    def dfs(node):
        if not node: return 
        return (node.val, dfs(node.left), dfs(node.right))
    return dfs(p)==dfs(q)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
print(sameTree(p, q))