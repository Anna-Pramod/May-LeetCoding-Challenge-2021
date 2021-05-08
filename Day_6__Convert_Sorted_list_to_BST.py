#Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

#For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

#Input: head = [-10,-3,0,5,9]
#Output: [0,-3,9,-10,null,5]
#Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n=0
        cur = head
        while (cur):
            cur = cur.next
            n+=1
            
        self.head = head
        
        def rec(st,end):
            if st>end:
                return None
            
            mid = (st+end)//2
            
            #left
            left = rec(st,mid-1)
            
            #root
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            
            #right
            root.right = rec(mid+1,end)
            
            return root
        return rec(0,n-1)
      
     # Your input : [-10,-3,0,5,9]
    #Your answer : [0,-10,5,null,-3,null,9]
    
    #Runtime: 52 ms
