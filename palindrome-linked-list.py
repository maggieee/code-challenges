# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current = head
        list1 = []
        
        while current is not None:
            list1.append(current.val)
            current = current.next
        
        return list1 == list1[::-1]