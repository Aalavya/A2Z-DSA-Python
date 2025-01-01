'''
GFG :> https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1

Given a BST and a number X, find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.

If Ceil could not be found, return -1.

Example 1:

Input: root = [5, 4, 6, 3, N, N, 7, 1], X = 3
      5
    /   \
   1     7
    \
     2 
      \
       3
Output: 3
Explanation: We find 3 in BST, so ceil of 3 is 3.
Example 2:

Input: root = [10, 5, 11, 4, 7, N, N, N, N, N, 8], X = 6
     10
    /  \
   5    11
  / \ 
 4   7
      \
       8
Output: 7
Explanation: We find 7 in BST, so ceil of 6 is 7.
Your task:
You don't need to read input or print anything. Just complete the function findCeil() to implement ceil in BST which returns the ceil of X in the given BST.

Constraints:
1 <= Number of nodes <= 105
1 <= Value of nodes<= 105

'''





def ceil(root,inp):
     if not root :
          return None 
     
     cValue  = -1 
     
     while root :
          
          if root.val == inp :
               cValue = root.val 
               return cValue 
          if root.val < inp :
              
               root = root.right 
               
          else :
               cValue = root.val 
               root = root.left 
               
     return cValue
               