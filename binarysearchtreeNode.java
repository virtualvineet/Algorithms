import java.io.*;

public class binarysearchtreeNode{
  int item;
  binarysearchtreeNode parent;
  binarysearchtreeNode left;
  binarysearchtreeNode right;
 
  public  binarysearchtreeNode ( int i , binarysearchtreeNode p, binarysearchtreeNode l, binarysearchtreeNode r){
  item = i;
  parent = p;
  left = l;
  right = r;
  }
  
  public  binarysearchtreeNode(){
  item =0;
  parent = null;
  left =null;
  right = null;
   }
 
  public int insertElement( int newitem, binarysearchtreeNode node){

  binarysearchtreeNode b2 = new binarysearchtreeNode(newitem, null, null, null);

  if(newitem > node.item) {
  //enter in the left node
  node.left = b2; 
  }
  else {
  //Enter in the right node
  node.right =b2; 
  }
  return 1;
  }
  
   public void visit( binarysearchtreeNode node){
     System.out.println(node.item);
   }

  //traverse the binary tree 
  //DFS search  
  public void inordertraverse (binarysearchtreeNode Node) {
   if (Node.left !=null)
      inordertraverse (Node.left);
   this.visit(Node);
   if (Node.right !=null)
      inordertraverse (Node.right);
   
  }

   public void preordertraverse (binarysearchtreeNode Node) {
   this.visit(Node);
   if (Node.left !=null)
      preordertraverse (Node.left);
   if (Node.right !=null)
      preordertraverse (Node.right);
   
  }
  
  public void postordertraverse (binarysearchtreeNode Node) {
   if (Node.left !=null)
      postordertraverse (Node.left);
   if (Node.right !=null)
      postordertraverse (Node.right);
   this.visit(Node);
   
  }


  public static void main ( String [] arg){
  
  System.out.println("Binary Search tree simulation\n");
  binarysearchtreeNode b1 =  new binarysearchtreeNode (20, null, null, null);
  b1.insertElement(10, b1);
  b1.insertElement(24, b1);
  System.out.println("In order traversal");
  b1.inordertraverse(b1);
  System.out.println("pre order traversal");
  b1.preordertraverse(b1);
  System.out.println("post order traversal");
  b1.postordertraverse(b1);
  }

}
