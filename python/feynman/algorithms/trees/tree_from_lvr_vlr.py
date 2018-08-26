from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
--- Idea 1 ---
Given a preorder, and inorder traversal of a binary tree,
construct the binary tree.

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
queue = []

Firstly, we can always get the root from popping the preorder.
So, we perform that action.

preorder = [9,20,15,7]
inorder = [9,3,15,20,7]
queue = []
root = TreeNode(3) 

--- Tree ---
3--\
------------

--- Idea 2 ---
I think we use the preorder traversal to guide our construction,
and the inorder traversal to remove ambiguities.

--- Idea 3 ---
I mean if we had the null nodes in the preorder traversal,
then we can reconstruct the tree.

Can we simply mutate preorder to insert the null nodes whenever necessary?

--- Idea 4 ---
preorder = [9,20,15,7]
inorder = [9,3,15,20,7]
queue = []

3 = preorder.popleft()
root = TreeNode(3)

3--\

preorder = [<root><left_subtree><right_subtree>]
inorder = [<left_subtree><root><right_subtree>]

1. Get root from preorder
2. Construct left subtree
3. Construct right subtree
"""
def build_tree(preorder, inorder):
    preorder = deque(preorder)
    inorder = deque(inorder)
    # queue = deque()
    root = TreeNode(preorder.popleft())
    build_subtree(preorder, inorder, root)
    
def build_subtree(preorder, inorder, parent):
    """
    preorder = [<left_subtree><right_subtree>]
    inorder = [<left_subtree><root><right_subtree>]
    preorder = [9,20,15,7]
    inorder = [9,3,15,20,7]
    """
    root = TreeNode(preorder.popleft())
    return root
    
    