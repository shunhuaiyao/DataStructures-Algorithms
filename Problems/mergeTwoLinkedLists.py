# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Merge two sorted linked lists and return it as a new list.
        Example,
        Input: 1->2->4, 1->3->4
        Output: 1->1->2->3->4->4
        """
        
        dummy = ListNode(None)
        curNode = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            curNode = curNode.next
        curNode.next = l1 or l2
        return dummy.next
        
        
        """
        '''
        Time complexity: O(len(l1)+len(l2))
        '''
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = ListNode(None)
        curNode = dummy
        curNode1 = l1
        curNode2 = l2
        while curNode1 != None or curNode2 != None:
            if curNode1 != None and curNode2 != None:
                if curNode1.val <= curNode2.val:
                    curNode.next = curNode1
                    curNode1 = curNode1.next
                else:
                    curNode.next = curNode2
                    curNode2 = curNode2.next
            elif curNode1 == None:
                curNode.next = curNode2
                curNode2 = curNode2.next
            else:
                curNode.next = curNode1
                curNode1 = curNode1.next
            curNode = curNode.next
        return dummy.next
        """