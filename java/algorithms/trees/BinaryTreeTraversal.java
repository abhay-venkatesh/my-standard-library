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

  public static void printBinaryTree(BinaryTreeNode root) {
    // TODO:
    printBinaryTreeLevel(root, getBinaryTreeDepth(root));
    Queue<BinaryTreeNode> queue = new LinkedList<BinaryTreeNode>();
    queue.add(root);
    while(!queue.isEmpty()) {
      BinaryTreeNode node = queue.remove();
      if(node.left != null) {
        printBinaryTreeLevel(node.left, getBinaryTreeDepth(node));
        queue.add(node.left);
      }
      if(node.right != null) {
        printBinaryTreeLevel(node.right, getBinaryTreeDepth(node));
        queue.add(node.right);
      }
    }
  }

  private static void printBinaryTreeLevel(BinaryTreeNode root, int height) {
    System.out.print(root.val);
    for(int i = 0; i < ((2*height) + 1); i++) {
      System.out.print("-");
    }
    System.out.print("\\");
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
