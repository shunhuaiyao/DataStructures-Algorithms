# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Given a linked list,
        remove the n-th node from the end of list and return its head.
        Example,
        Given linked list: 1->2->3->4->5, and n = 2,
        the linked list becomes 1->2->3->5.
        All given n will always be valid.
        """
        """
        Two-pass Solution
        """
        front = ListNode(None)
        front.next = head
        curNode = front
        lenListNode = 0
        while curNode.next != None:
            curNode = curNode.next
            lenListNode += 1
        target = lenListNode - n + 1
        
        preNode = front
        curNode = front
        i = 0
        while curNode.next != None:
            preNode = curNode
            curNode = curNode.next
            i += 1
            if i == target:
                preNode.next = curNode.next
                break
                
        return front.next