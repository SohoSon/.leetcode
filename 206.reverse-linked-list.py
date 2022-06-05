#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # #iteratively
        # prev, curr = None, head
        # #> 1 - 2 - 3 - none
        # while curr: # 1 (while loop)
        #     temp = curr.next #save 2
        #     curr.next = prev # 1 -> none
        #     prev = curr # prev = 1
        #     curr = temp # curr = 2
        # return prev

        ###################################
        #recursively

        if not head or not head.next:  #base case
            return head # return 5
            #curr head = 4
        else:
            newhead = self.reverseList(head.next) # assuming 5 #not pointer
            head.next.next = head # 5 - > 4
        head.next = None # 4 -> none

        return newhead #what it passed is none 5... all the time.. finally undetstood

# @lc code=end

