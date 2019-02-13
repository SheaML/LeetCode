# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        num1=str()
        num1 = str(l1.val) + num1
        while True:
            if l1.next == None:
                break
            l1=l1.next    
            num1 = str(l1.val) + num1
        
        num2=str()
        num2 = str(l2.val) + num2
        while True:
            if l2.next == None:
                break
            l2=l2.next    
            num2 = str(l2.val) + num2

        
        ans = int(num1) + int(num2)
        strans=str(ans)
        
        ansList=[int(i) for i in strans[::-1]]
        return ansList
        
