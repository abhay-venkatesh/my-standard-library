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
2-\ 3-\
4 5 6 7

queue = []
prev = 1
num_nodes_on_level = 0
node = 1
"""


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = deque([root])
        prev = None
        num_nodes_on_level = 1
        level = 1
        while queue:
            node = queue.pop()
            num_nodes_on_level -= 1

            if prev and num_nodes_on_level == 0:
                node.next = prev
            prev = node

            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)
            num_nodes_on_level += 2


def main():
    pass


if __name__ == '__main__':
    main()
