import java.util.*;
import java.lang.*;

class BinaryTreeNode {
  int val;
  BinaryTreeNode left;
  BinaryTreeNode right;

  public BinaryTreeNode(int val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BinaryTreeTraversal {
  /*
  1------\
  2-\ 3-\


  */

  public static void printBinaryTree(BinaryTreeNode root) {
    // TODO:
    Queue<BinaryTreeNode> queue = new LinkedList<BinaryTreeNode>();
    queue.add(root);
    int level = 0;
    int height = getBinaryTreeDepth(root);
    int num_nodes_on_level = 1;
    int num_nodes_left_on_level = 1;
    while(!queue.isEmpty()) {
      BinaryTreeNode node = queue.remove();
      printBinaryTreeLevel(node, level, height);
      num_nodes_left_on_level -= 1;
      if(num_nodes_left_on_level == 0) {
        level++;
        num_nodes_on_level *= 2;
        num_nodes_left_on_level = num_nodes_on_level;
        height--;
        System.out.println();
      }
      if(node.left != null) queue.add(node.left);
      if(node.right != null) queue.add(node.right);
    }
  }

  private static void printBinaryTreeLevel(
    BinaryTreeNode node,
    int level,
    int height
  ) {
    System.out.print(node.val);
    for(int i = 0; i < ((3*(height-2)) + 1); i++) {
      System.out.print("-");
    }
    if(height-1 != 0) System.out.print("\\ ");
    else System.out.print(" ");
  }

  public static int getBinaryTreeDepth(BinaryTreeNode root) {
    if(root == null) return 0;
    return Math.max(1 + getBinaryTreeDepth(root.left),
                    1 + getBinaryTreeDepth(root.right));
  }

  public static List<Integer> iterativeInOrderTraversal(BinaryTreeNode root) {
    // TODO:
    return null;
  }

  public static void recursiveInOrderTraversal(BinaryTreeNode root) {
    if(root == null) return;
    recursiveInOrderTraversal(root.left);
    System.out.println(root.val);
    recursiveInOrderTraversal(root.right);
  }

  public static int kthSmallestElementInBST(BinaryTreeNode root, int k) {
    // TODO: kth item in in-order traversal
    return 0;
  }

  public static boolean validateBST(BinaryTreeNode root) {
    // TODO:
    return false;
  }

  public static BinaryTreeNode constructBST() {
    /*
    5-----\
    3-\ 7-\
    1 4 6 8
    */
    BinaryTreeNode root = new BinaryTreeNode(5);
    BinaryTreeNode three = new BinaryTreeNode(3);
    BinaryTreeNode seven = new BinaryTreeNode(7);
    root.left = three;
    root.right = seven;
    three.left = new BinaryTreeNode(1);
    three.right = new BinaryTreeNode(4);
    seven.left = new BinaryTreeNode(6);
    seven.right = new BinaryTreeNode(8);
    return root;
  }

  public static void main(String[] args) {
    BinaryTreeNode root = constructBST();
    printBinaryTree(root);
  }
}
