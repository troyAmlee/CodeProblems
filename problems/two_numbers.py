'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
Accepted
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack = []
        stack2 = []
        stack3 = []
        returningList = []
        str1 = ""
        str2 = ""
        
        while(l1 is not None):
            stack.append(str(l1.val))
            l1 = l1.next
            
        while(l2 is not None):
            stack2.append(str(l2.val))
            l2 = l2.next
        
        print(f"stack {stack} stack2 {stack2}")
        
        for i in stack:
            str1 += i
            
        converted1 = int(str1)
            
        for j in stack2:
            str2 += j
            
        converted2 = int(str2)
        
        ret_node = converted2 + converted1
        
        stringify = str(ret_node)
        
        splitted = list(stringify)
        
        print(splitted)
        
        for i in range(len(splitted)):
            num = splitted.pop()
            stack3.append(int(num))
            
        def add_to_tail(node, item):
            newnode = ListNode(item)
            if(node == None):
                node = newnode
            else:
                ptr = node
                while(ptr.next != None):
                    ptr = ptr.next
                    
                ptr.next = newnode
                
            return node
                
        root = None
        for i in range(0, len(stack3), 1):
            root = add_to_tail(root, stack3[i]) 

        return root 