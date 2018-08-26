from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree_from_full_preorder(preorder):
    """
    preorder = [3,9,NULL,NULL,20,15,7]
    """
    if not preorder:
        return
        
    rootval = preorder.popleft()
    if rootval == "NULL":
        return 
        
    root = TreeNode(rootval)
    root.left = build_tree_from_full_preorder(preorder)
    root.right = build_tree_from_full_preorder(preorder)
    
    return root
    
def build_full_preorder_iter(preorder):
    stack = [preorder.popleft()]
    while stack:
        nodeval = stack.pop()
        if nodeval == "NULL":
            return

        
    
    
    