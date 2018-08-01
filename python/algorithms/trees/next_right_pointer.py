from collections import deque

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
"""
1----\
2-->3-\
4 5 6>7

queue = [4, 5]
node = 6
num_nodes_on_level = 2
prev = 7
level = 2
new_level = False 
"""


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        queue = deque([root])
        prev = None
        level = 0
        num_nodes_on_level = 1
        new_level = True
        while queue:
            node = queue.pop()
            num_nodes_on_level -= 1

            if not new_level:
                node.next = prev
            prev = node

            new_level = False
            if num_nodes_on_level == 0:
                level += 1
                num_nodes_on_level += 2 ** level 
                new_level = True

            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)



def main():
    pass


if __name__ == '__main__':
    main()
