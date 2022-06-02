#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #tempSum
        #temp_l1
        #temp_l2
        #我目前的猜想是，正序的linked list，可以用这种 先取值，再历遍的方法。
        #如果是从尾向前（例如二叉树，我们要用recursively method）
        #总之先写写看
        tempout = ListNode()
        ListHead = ListNode()  #dummyHead feature, the Node we need to return(curr at tail)
        tempout = ListHead
        temp_l1 = l1
        temp_l2 = l2
        val1 = 0
        val2 = 0
        carry = 0
        sum = 0
        while(temp_l1 != None or temp_l2 != None):  
            if(temp_l1 != None):      #问题2： 如果不chekc 是否为none，那么当tamp为none时，val就得不到更新（出现错误，因为nonenode里没有val）
                val1 = temp_l1.val
            else:
                val1 = 0
            if(temp_l2 != None):
                val2 = temp_l2.val
            else:
                val2 = 0
            sum = carry + val1 + val2
            if (carry + val1 + val2 >= 10):  #问题3：重复， 的代码 增加出错的几率，即使是小的问题，也很难debug（miss carry+）
                carry = 1
            else: 
                carry = 0
            #carry = sum // 10
            
            # tempout.val = sum
            # tempout.next = ListNode()
            # tempout = tempout.next
            tempout.next = ListNode(sum % 10)   #问题1. 用dummyhead 避免出现最后一位多出next，（因为在while循环中，对next的initializa会让其tail多一个空node）
            tempout = tempout.next


            if (temp_l1 != None):
                temp_l1 = temp_l1.next
            
            if(temp_l2 != None):
                temp_l2 = temp_l2.next

        if(carry > 0):
            tempout.next = ListNode(1)
        
        return ListHead.next


# @lc code=end

