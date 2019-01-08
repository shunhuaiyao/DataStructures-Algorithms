# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order and each of their nodes contain a single digit.
        Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        Example,
        (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8), which means 342 + 465 = 807.
        """
        curNode = dummyHead = ListNode(0)
        node1 = l1
        node2 = l2
        carry = 0
        while node1 != None or node2 != None:
            x = y = 0
            if node1 != None:
                x = node1.val
            if node2 != None:
                y = node2.val
            sum = x + y + carry
            carry = sum // 10
            curNode.next = ListNode(sum % 10)
            curNode = curNode.next
            if node1 != None:
                node1 = node1.next
            if node2 != None:
                node2 = node2.next
        if carry:
            curNode.next = ListNode(carry)  
        return dummyHead.next
            
            
        