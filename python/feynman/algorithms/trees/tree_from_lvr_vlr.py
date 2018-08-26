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
    """
    preorder = [3,9,NULL,NULL,20,15,7]
    
    3---\
    9
    """
    stack = [preorder.popleft()]
    parent = None
    root = None
    while stack:
        node_val = stack.pop()
        if not root:
            root = TreeNode(node_val)
            parent = root
        else:
            if node_val != "NULL":
                node = TreeNode(node_val)
                parent.left = node
                parent = node
            else:
                pass
                
            

        
    
    
    