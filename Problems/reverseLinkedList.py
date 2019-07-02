# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseLinkedList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Sol 1:
        iterative function
        """
        if head == None or head.next == None:
            return head
        previousNode = None
        currentNode = head
        nextNode = head.next
        while head.next != None:
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next
        currentNode.next = previousNode
        return currentNode


        """
        Sol 2:
        recursive function
        """
        if head == None or head.next == None:
            return head
        reversedList = self.reverseLinkedList(head.next)
        head.next.next = head
        head.next = None
        return reversedList