from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def build_tree(preorder, inorder):
    """
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    3-----\
    9-\ 20-\
        15 7
        
    preorder = [<root><left subtree><right subtree>]
    inorder = [<left subtree><root><right subtree>]
    
    --- Test Run ---
    --- build_tree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]) ---
    i = 1
    
    3-----\
    9-\
    
    --- build_tree(preorder = [20,15,7], inorder = [15,20,7]) ---
    root = TreeNode(20)
    i = 1
    
    20-\
    15 7

    --- build_tree(preorder = [7], inorder = [7]) ---
    
    """
    if not preorder:
        return 

    root = TreeNode(preorder[0])
    i = 0
    while inorder[i] != root.val:
        i += 1
    root.left = build_tree(preorder[1:i+1], inorder[:i])
    root.right = build_tree(preorder[i+1:], inorder[i+1:])
    return root
        
    
    


        
    
    
